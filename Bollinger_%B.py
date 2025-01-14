import pandas as pd

def bollinger_band_percent_b(df, period=20, std_dev=2):
    """
    Calculate the Bollinger Band %B for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Close' prices and 'Symbol' column.
    period (int): Lookback period for the Bollinger Bands calculation.
    std_dev (int): Number of standard deviations for the Bollinger Bands.

    Returns:
    DataFrame: The DataFrame with Bollinger Band %B values for each Symbol group.
    """
    # Group by 'Symbol' and apply the Bollinger Band %B calculation for each group
    def calculate_bollinger_band_percent_b(group):
        # Calculate the Simple Moving Average (SMA)
        sma = group['Close'].rolling(window=period).mean()

        # Calculate the standard deviation of the close prices
        rolling_std = group['Close'].rolling(window=period).std()

        # Calculate the upper and lower Bollinger Bands
        upper_band = sma + (rolling_std * std_dev)
        lower_band = sma - (rolling_std * std_dev)

        # Calculate Bollinger Band %B
        percent_b = (group['Close'] - lower_band) / (upper_band - lower_band)

        return percent_b

    # Apply the function to each group
    df['Bollinger_%B'] = df.groupby('Symbol').apply(calculate_bollinger_band_percent_b).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Close' and 'Symbol' columns
df['Bollinger_%B'] = bollinger_band_percent_b(df)

# Display the DataFrame with Bollinger Band %B values
print(df[['Timestamp', 'Symbol', 'Close', 'Bollinger_%B']])
