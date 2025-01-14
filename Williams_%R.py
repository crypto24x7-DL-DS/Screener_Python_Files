import pandas as pd

def williams_r_with_grouping(df, period=14):
    """
    Calculate the Williams %R for a given DataFrame, grouped by the 'Symbol' column.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns.
    period (int): Lookback period for the Williams %R calculation.

    Returns:
    DataFrame: A DataFrame with the original data and an additional 'Williams_%R' column.
    """
    def calc_williams_r(group):
        # Calculate the highest high and lowest low over the given period
        high_max = group['High'].rolling(window=period).max()
        low_min = group['Low'].rolling(window=period).min()

        # Calculate Williams %R
        williams_r = -100 * ((high_max - group['Close']) / (high_max - low_min))
        return williams_r

    # Apply calculation for each group
    df['Williams_%R'] = df.groupby('Symbol').apply(calc_williams_r).reset_index(level=0, drop=True)
    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # Ensure Timestamp is a datetime object if needed
df = df.sort_values(['Symbol', 'Timestamp'])  # Sort by Symbol and Timestamp for proper rolling calculation

df_with_williams_r = williams_r_with_grouping(df)

# Display the DataFrame with Williams %R values
print(df_with_williams_r[['Timestamp', 'Symbol', 'High', 'Low', 'Close', 'Williams_%R']])
