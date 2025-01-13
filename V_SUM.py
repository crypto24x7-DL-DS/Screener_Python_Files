def calculate_sum(df, column, window):
    """
    Calculate the rolling sum for a specified window for each symbol.

    Parameters:
    df (DataFrame): DataFrame containing the data with 'Symbol' column.
    column (str): The column for which to calculate the rolling sum (e.g., 'Volume').
    window (int): The window length for calculating the sum.

    Returns:
    DataFrame: The DataFrame with rolling sum values for each symbol.
    """
    # Define a function to calculate rolling sum for each symbol
    def calculate_for_symbol(symbol_df):
        rolling_sum = symbol_df[column].rolling(window=window).sum()
        return rolling_sum

    # Group by 'Symbol' and apply the rolling sum calculation for each group
    df[f'{column}_Sum'] = df.groupby('Symbol').apply(calculate_for_symbol).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Volume' and 'Symbol' columns
df = calculate_sum(df, 'Volume', 7)  # For a 7-period rolling sum of 'Volume'

# Display the DataFrame with rolling sum values
print(df[['Timestamp', 'Symbol', 'Volume', 'Volume_Sum']])
