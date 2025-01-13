def calculate_rolling_close(df, window):
    """
    Calculate the rolling Close price for a specified window length for each symbol.

    Parameters:
    df (DataFrame): DataFrame with 'Close' and 'Symbol' columns.
    window (int): The window length for calculating the rolling Close.

    Returns:
    DataFrame: The DataFrame with rolling Close values for each symbol.
    """
    # Define a function to calculate the rolling close for each symbol
    def calculate_for_symbol(symbol_df):
        rolling_close = symbol_df['Close'].rolling(window=window).mean()  # You can use .mean(), .max(), or .min() depending on your needs
        return rolling_close

    # Group by 'Symbol' and apply the rolling close calculation for each group
    df['Rolling_Close'] = df.groupby('Symbol').apply(calculate_for_symbol).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Close' and 'Symbol' columns
df = calculate_rolling_close(df, 5)  # Average Close for each rolling 5-period window

# Display the DataFrame with rolling close prices
print(df[['Timestamp', 'Symbol', 'Close', 'Rolling_Close']])
