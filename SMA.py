def calculate_sma(df, window):
    """
    Calculate the Simple Moving Average (SMA) for each symbol in the DataFrame.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Close'].
    window (int): The window length for calculating the SMA.

    Returns:
    DataFrame: Original DataFrame with a new SMA column calculated separately for each symbol.
    """
    # Group by 'Symbol' and calculate SMA for each group
    df[f'SMA_{window}'] = df.groupby('Symbol')['Close'].transform(lambda x: x.rolling(window=window).mean())
    return df

# Example usage:
# Calculate SMA for 50-period and 200-period for all symbols
df = calculate_sma(df, 50)
df = calculate_sma(df, 200)

# Output example
print(df[['Symbol', 'Timestamp', 'Close', f'SMA_{50}', f'SMA_{200}']])
