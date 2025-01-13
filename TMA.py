def calculate_tma(df, window):
    """
    Calculate the Triangular Moving Average (TMA) for a specified window, separately for each symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Close'].
    window (int): The window length for calculating the TMA.

    Returns:
    DataFrame: Original DataFrame with a new TMA column calculated separately for each symbol.
    """
    # Group by 'Symbol' and calculate TMA for each group
    df[f'TMA_{window}'] = df.groupby('Symbol')['Close'].transform(
        lambda x: x.rolling(window=window).mean().rolling(window=window).mean()
    )
    return df

# Example usage:
# Assuming 'df' is your DataFrame with at least 'Symbol' and 'Close' columns
df = calculate_tma(df, 20)  # For a 20-period TMA

# Display the DataFrame with TMA values and Symbol column
print(df[['Symbol', 'Timestamp', 'Close', f'TMA_20']])
