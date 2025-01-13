def calculate_pivot_point(df):
    """
    Calculate the Pivot Point (PP) and its support and resistance levels for each row in the DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', 'Close', and 'Symbol' columns.

    Returns:
    DataFrame: DataFrame with calculated Pivot Point (PP), Support and Resistance levels (S1, S2, R1, R2) for each symbol.
    """
    # Define a function to calculate pivot points for each symbol
    def calculate_for_symbol(symbol_df):
        # Calculate the Pivot Point (PP)
        symbol_df['Pivot_Point'] = (symbol_df['High'] + symbol_df['Low'] + symbol_df['Close']) / 3

        # Calculate Support and Resistance levels
        symbol_df['Support_1'] = (2 * symbol_df['Pivot_Point']) - symbol_df['High']
        symbol_df['Support_2'] = symbol_df['Pivot_Point'] - (symbol_df['High'] - symbol_df['Low'])
        symbol_df['Resistance_1'] = (2 * symbol_df['Pivot_Point']) - symbol_df['Low']
        symbol_df['Resistance_2'] = symbol_df['Pivot_Point'] + (symbol_df['High'] - symbol_df['Low'])

        return symbol_df

    # Group by 'Symbol' and apply the pivot point calculation for each group
    df = df.groupby('Symbol').apply(calculate_for_symbol).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'High', 'Low', 'Close', and 'Symbol' columns
df = calculate_pivot_point(df)

# Display the DataFrame with Pivot Point and support/resistance levels
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Close', 'Pivot_Point', 'Support_1', 'Support_2', 'Resistance_1', 'Resistance_2']])
