def calculate_rolling_low(df, window):
    """
    Calculate the rolling Low price for a specified window length for each symbol.

    Parameters:
    df (DataFrame): DataFrame with 'Low' and 'Symbol' columns.
    window (int): The window length for calculating the rolling Low.

    Returns:
    DataFrame: The DataFrame with rolling Low values for each symbol.
    """
    # Define a function to calculate the rolling low for each symbol
    def calculate_for_symbol(symbol_df):
        rolling_low = symbol_df['Low'].rolling(window=window).min()
        return rolling_low

    # Group by 'Symbol' and apply the rolling low calculation for each group
    df['Rolling_Low'] = df.groupby('Symbol').apply(calculate_for_symbol).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Low' and 'Symbol' columns
df = calculate_rolling_low(df, 5)  # Min Low for each rolling 5-period window

# Display the DataFrame with rolling low prices
print(df[['Timestamp', 'Symbol', 'Low', 'Rolling_Low']])
