def calculate_std(df, window):
    """
    Calculate the rolling Standard Deviation (STD) for a specified window for each symbol.

    Parameters:
    df (DataFrame): DataFrame with 'Close' and 'Symbol' columns.
    window (int): The window length for calculating the STD.

    Returns:
    DataFrame: The DataFrame with STD values for each symbol.
    """
    # Define a function to calculate STD for each symbol
    def calculate_for_symbol(symbol_df):
        std = symbol_df['Close'].rolling(window=window).std()
        return std

    # Group by 'Symbol' and apply the STD calculation for each group
    df['STD'] = df.groupby('Symbol').apply(calculate_for_symbol).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Close' and 'Symbol' columns
df = calculate_std(df, 20)  # For a 20-period rolling STD

# Display the DataFrame with STD values
print(df[['Timestamp', 'Symbol', 'Close', 'STD']])
