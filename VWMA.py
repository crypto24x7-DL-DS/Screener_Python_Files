def calculate_vwma(df, window):
    """
    Calculate the Volume-Weighted Moving Average (VWMA) for a specified window for each symbol.

    Parameters:
    df (DataFrame): DataFrame with 'Close', 'Volume', and 'Symbol' columns.
    window (int): The window length for calculating the VWMA.

    Returns:
    DataFrame: The DataFrame with VWMA values for each symbol.
    """
    # Define a function to calculate VWMA for each symbol
    def calculate_for_symbol(symbol_df):
        price_volume = symbol_df['Close'] * symbol_df['Volume']
        vwma = price_volume.rolling(window=window).sum() / symbol_df['Volume'].rolling(window=window).sum()
        return vwma

    # Group by 'Symbol' and apply the VWMA calculation for each group
    df['VWMA'] = df.groupby('Symbol').apply(calculate_for_symbol).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Close', 'Volume', and 'Symbol' columns
df = calculate_vwma(df, 20)  # For a 20-period VWMA

# Display the DataFrame with VWMA values
print(df[['Timestamp', 'Symbol', 'Close', 'Volume', 'VWMA']])
