import pandas as pd

def schaff_trend_cycle(df, fast_length=23, slow_length=50, signal_length=9):
    """
    Calculate the Schaff Trend Cycle (STC) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Close', 'High', and 'Low' prices, and 'Symbol'.
    fast_length (int): The fast length for the EMA (usually 23).
    slow_length (int): The slow length for the EMA (usually 50).
    signal_length (int): The length for the Signal line EMA (usually 9).

    Returns:
    DataFrame: The DataFrame with STC values for each Symbol group.
    """

    # Group by 'Symbol' and apply the STC calculation for each group
    def calculate_stc(group):
        # Calculate the MACD Line
        fast_ema = group['Close'].ewm(span=fast_length, adjust=False).mean()
        slow_ema = group['Close'].ewm(span=slow_length, adjust=False).mean()
        macd_line = fast_ema - slow_ema

        # Calculate the Signal Line
        signal_line = macd_line.ewm(span=signal_length, adjust=False).mean()

        # Calculate the Stochastic (9-period)
        low_min = group['Low'].rolling(window=9).min()
        high_max = group['High'].rolling(window=9).max()
        stoch = ((group['Close'] - low_min) / (high_max - low_min)) * 100

        # Calculate the Schaff Trend Cycle (STC)
        stc = macd_line * stoch
        return stc

    # Apply the function to each group
    df['STC'] = df.groupby('Symbol').apply(calculate_stc).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Close', 'High', 'Low', and 'Symbol' columns
df['STC'] = schaff_trend_cycle(df)

# Display the DataFrame with STC values
print(df[['Timestamp', 'Symbol', 'Close', 'High', 'Low', 'STC']])
