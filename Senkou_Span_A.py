import pandas as pd

def ichimoku_span_a(df, conversion_period=9, base_period=26, span_offset=26):
    """
    Calculate the Ichimoku Span A (Senkou Span A) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High' and 'Low' columns.
    conversion_period (int): The period for the Conversion Line (Tenkan-sen), default is 9.
    base_period (int): The period for the Base Line (Kijun-sen), default is 26.
    span_offset (int): The period to shift Senkou Span A forward, default is 26.

    Returns:
    DataFrame: DataFrame with the calculated Senkou Span A for each Symbol.
    """
    # Group by Symbol and calculate the Span A for each group
    df['Senkou_Span_A'] = df.groupby('Symbol').apply(
        lambda x: ((x['High'].rolling(window=conversion_period).max() + x['Low'].rolling(window=conversion_period).min()) / 2 +
                  (x['High'].rolling(window=base_period).max() + x['Low'].rolling(window=base_period).min()) / 2) / 2
    ).shift(span_offset).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', and 'Low' columns
df = ichimoku_span_a(df)

# Display the DataFrame with Senkou Span A values
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Senkou_Span_A']])
