def calculate_r1(df):
    """
    Calculate the first resistance level (R1) for each row in the DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', 'Close' columns.

    Returns:
    DataFrame: DataFrame with calculated Resistance 1 (R1).
    """
    df['Resistance_1'] = (2 * df['Pivot_Point']) - df['Low']
    return df

def calculate_r2(df):
    """
    Calculate the second resistance level (R2) for each row in the DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', 'Close' columns.

    Returns:
    DataFrame: DataFrame with calculated Resistance 2 (R2).
    """
    df['Resistance_2'] = df['Pivot_Point'] + (df['High'] - df['Low'])
    return df

def calculate_s1(df):
    """
    Calculate the first support level (S1) for each row in the DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', 'Close' columns.

    Returns:
    DataFrame: DataFrame with calculated Support 1 (S1).
    """
    df['Support_1'] = (2 * df['Pivot_Point']) - df['High']
    return df

def calculate_s2(df):
    """
    Calculate the second support level (S2) for each row in the DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', 'Close' columns.

    Returns:
    DataFrame: DataFrame with calculated Support 2 (S2).
    """
    df['Support_2'] = df['Pivot_Point'] - (df['High'] - df['Low'])
    return df

def calculate_support_resistance(df):
    """
    Apply support and resistance level calculations after the Pivot Point calculation,
    grouping by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', 'Close', and 'Symbol' columns.

    Returns:
    DataFrame: DataFrame with all support and resistance levels for each symbol.
    """
    # Group by 'Symbol' and apply the support/resistance calculations for each group
    def apply_levels(symbol_df):
        symbol_df = calculate_r1(symbol_df)
        symbol_df = calculate_r2(symbol_df)
        symbol_df = calculate_s1(symbol_df)
        symbol_df = calculate_s2(symbol_df)
        return symbol_df

    df = df.groupby('Symbol').apply(apply_levels).reset_index(level=0, drop=True)

    return df

# Assuming 'df' is your DataFrame with 'High', 'Low', 'Close', and 'Symbol' columns
df = calculate_pivot_point(df)  # First, calculate Pivot Point

# Then, calculate each support and resistance level for each symbol
df = calculate_support_resistance(df)

# Display the DataFrame with all levels
print(df[['Timestamp', 'Symbol', 'Pivot_Point', 'Support_1', 'Support_2', 'Resistance_1', 'Resistance_2']])
