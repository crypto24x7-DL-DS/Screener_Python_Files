import pandas as pd

def calculate_atr_with_symbol(df, window_length=14):
    """
    Calculate the Average True Range (ATR) for each symbol in the dataset.
    Resets calculations when the 'Symbol' changes.

    Parameters:
    df (DataFrame): DataFrame with columns 'Symbol', 'High', 'Low', 'Close'.
    window_length (int): The period for the ATR calculation (default is 14).

    Returns:
    DataFrame: Original DataFrame with an added 'ATR' column.
    """
    def calculate_atr_group(group):
        # Calculate True Range (TR)
        group['High-Low'] = group['High'] - group['Low']
        group['High-Close'] = abs(group['High'] - group['Close'].shift(1))
        group['Low-Close'] = abs(group['Low'] - group['Close'].shift(1))
        group['True_Range'] = group[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)

        # Calculate ATR using a rolling mean of the True Range
        group['ATR'] = group['True_Range'].rolling(window=window_length).mean()

        # Drop intermediary columns for a cleaner output
        group = group.drop(columns=['High-Low', 'High-Close', 'Low-Close', 'True_Range'])
        return group

    # Apply calculation grouped by 'Symbol'
    df = df.groupby('Symbol', group_keys=False).apply(calculate_atr_group)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with columns: 'Timestamp', 'Symbol', 'High', 'Low', 'Close', etc.
df = calculate_atr_with_symbol(df, window_length=20)

# Display the DataFrame with the ATR column added
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Close', 'ATR']])
