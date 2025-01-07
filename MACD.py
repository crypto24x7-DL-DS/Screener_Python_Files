import pandas as pd

def calculate_macd_with_symbol(df, short_window=12, long_window=26, signal_window=9):
    """
    Calculate the MACD and Signal Line for each symbol in the dataset.
    Resets calculations when the 'Symbol' changes.

    Parameters:
    df (DataFrame): DataFrame with 'Symbol' and 'Close' columns.
    short_window (int): The period for the short EMA (default 12).
    long_window (int): The period for the long EMA (default 26).
    signal_window (int): The period for the signal line EMA (default 9).

    Returns:
    DataFrame: Original DataFrame with added 'MACD' and 'Signal_Line' columns.
    """
    def calculate_macd_group(group):
        # Calculate the short and long EMAs
        group['EMA_short'] = group['Close'].ewm(span=short_window, adjust=False).mean()
        group['EMA_long'] = group['Close'].ewm(span=long_window, adjust=False).mean()

        # Calculate MACD line
        group['MACD'] = group['EMA_short'] - group['EMA_long']

        # Calculate Signal Line
        group['Signal_Line'] = group['MACD'].ewm(span=signal_window, adjust=False).mean()

        # Drop intermediary EMA columns for a cleaner DataFrame
        group = group.drop(columns=['EMA_short', 'EMA_long'])
        return group

    # Apply calculation grouped by 'Symbol'
    df = df.groupby('Symbol', group_keys=False).apply(calculate_macd_group)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with columns: 'Timestamp', 'Symbol', 'Close', etc.
df = calculate_macd_with_symbol(df)

# Display the DataFrame with the MACD and Signal Line columns added
print(df[['Timestamp', 'Symbol', 'Close', 'MACD', 'Signal_Line']])
