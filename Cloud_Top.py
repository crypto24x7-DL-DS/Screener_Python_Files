import pandas as pd

def ichimoku_cloud_top(df, conversion_period=9, base_period=26, span_offset=26):
    """
    Calculate the Ichimoku Cloud Top (Senkou Span A) for a given DataFrame, grouped by 'Symbol'.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', and 'Symbol' columns.
    conversion_period (int): Period for the Conversion Line (Tenkan-sen), default is 9.
    base_period (int): Period for the Base Line (Kijun-sen), default is 26.
    span_offset (int): Period to shift the Cloud Top forward, typically 26.

    Returns:
    DataFrame: A DataFrame with the Cloud Top (Senkou Span A) for each Symbol.
    """
    # Group by 'Symbol'
    def calculate_cloud_top(symbol_df):
        # Conversion Line (Tenkan-sen)
        conversion_line = (symbol_df['High'].rolling(window=conversion_period).max() +
                           symbol_df['Low'].rolling(window=conversion_period).min()) / 2

        # Base Line (Kijun-sen)
        base_line = (symbol_df['High'].rolling(window=base_period).max() +
                     symbol_df['Low'].rolling(window=base_period).min()) / 2

        # Cloud Top (Senkou Span A)
        cloud_top = ((conversion_line + base_line) / 2).shift(span_offset)

        # Add Cloud Top to the DataFrame
        symbol_df['Cloud_Top'] = cloud_top

        return symbol_df

    # Apply the function to each group (grouped by 'Symbol')
    df = df.groupby('Symbol').apply(calculate_cloud_top)

    return df[['Timestamp', 'Symbol', 'High', 'Low', 'Cloud_Top']]

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low' columns
df = ichimoku_cloud_top(df)

# Display the DataFrame with Cloud Top
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Cloud_Top']])
