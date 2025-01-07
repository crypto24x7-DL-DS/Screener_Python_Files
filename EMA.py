def calculate_ema(df, window):
    """
    Calculate the Exponential Moving Average (EMA) for a specified window, separately for each symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Close'].
    window (int): The window length for calculating the EMA.

    Returns:
    DataFrame: Original DataFrame with a new EMA column calculated separately for each symbol.
    """
    # Group by 'Symbol' and calculate EMA for each group
    df[f'EMA_{window}'] = df.groupby('Symbol')['Close'].transform(lambda x: x.ewm(span=window, adjust=False).mean())
    return df

# Example usage:
# Assuming 'df' is your DataFrame with at least 'Symbol' and 'Close' columns
df = calculate_ema(df, 50)  # For a 50-period EMA
df = calculate_ema(df, 200)  # For a 200-period EMA

# Display the DataFrame with EMA values and Symbol column
print(df[['Symbol', 'Timestamp', 'Close', 'EMA_50', 'EMA_200']])
