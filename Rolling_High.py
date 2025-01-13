def calculate_rolling_high(df, window):
    """
    Calculate the rolling High price for a specified window length for each symbol.

    Parameters:
    df (DataFrame): DataFrame with 'High' and 'Symbol' columns.
    window (int): The window length for calculating the rolling High.

    Returns:
    DataFrame: The DataFrame with rolling High values for each symbol.
    """
    # Define a function to calculate the rolling high for each symbol
    def calculate_for_symbol(symbol_df):
        rolling_high = symbol_df['High'].rolling(window=window).max()
        return rolling_high

    # Group by 'Symbol' and apply the rolling high calculation for each group
    df['Rolling_High'] = df.groupby('Symbol').apply(calculate_for_symbol).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'High' and 'Symbol' columns
df = calculate_rolling_high(df, 5)  # Max High for each rolling 5-period window

# Display the DataFrame with rolling high prices
print(df[['Timestamp', 'Symbol', 'High', 'Rolling_High']])
