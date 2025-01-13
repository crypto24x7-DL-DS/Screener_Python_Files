import pandas as pd

def calculate_upper_bollinger_band(df, window=20, k=2):
    """
    Calculate the Upper Bollinger Band for the given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol' and 'Close' columns.
    window (int): The window length for calculating SMA and STD, default is 20.
    k (float): The multiplier for the standard deviation, default is 2.

    Returns:
    DataFrame: DataFrame with the calculated Upper Bollinger Band.
    """
    # Group by Symbol and apply calculations to each group
    df['SMA'] = df.groupby('Symbol')['Close'].rolling(window=window).mean().reset_index(level=0, drop=True)
    df['STD'] = df.groupby('Symbol')['Close'].rolling(window=window).std().reset_index(level=0, drop=True)

    # Calculate the Upper Bollinger Band
    df['Upper_BB'] = df['SMA'] + (k * df['STD'])

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol' and 'Close' columns
df = calculate_upper_bollinger_band(df)

# Display the DataFrame with Upper Bollinger Band
print(df[['Timestamp', 'Symbol', 'Close', 'Upper_BB']])
