import pandas as pd

def force_index(df, period=1):
    """
    Calculate the Force Index (FI) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Close', 'Volume', and 'Symbol' columns.
    period (int): The period for calculating the Force Index moving average (default is 1 for the original Force Index).

    Returns:
    DataFrame: The DataFrame with Force Index values for each Symbol group.
    """
    # Group by 'Symbol' and apply the Force Index calculation for each group
    def calculate_force_index(group):
        # Calculate the daily price change (current close - previous close)
        price_change = group['Close'].diff(periods=1)

        # Calculate the raw Force Index as price change multiplied by volume
        raw_fi = price_change * group['Volume']

        # Calculate the smoothed Force Index using an exponential moving average
        force_index_ema = raw_fi.ewm(span=period, adjust=False).mean()

        return force_index_ema

    # Apply the function to each group
    df['Force_Index'] = df.groupby('Symbol').apply(calculate_force_index).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Close', 'Volume', and 'Symbol' columns
df['Force_Index'] = force_index(df, period=13)

# Display the DataFrame with Force Index values
print(df[['Timestamp', 'Symbol', 'Close', 'Volume', 'Force_Index']])
