import pandas as pd

def ichimoku_span_b(df, span_b_period=52, span_offset=26):
    """
    Calculate the Ichimoku Span B (Senkou Span B) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High' and 'Low' columns.
    span_b_period (int): The period for calculating the Span B, default is 52.
    span_offset (int): The period to shift Senkou Span B forward, default is 26.

    Returns:
    DataFrame: DataFrame with the calculated Senkou Span B for each Symbol.
    """
    # Group by Symbol and calculate the Span B for each group
    df['Senkou_Span_B'] = df.groupby('Symbol').apply(
        lambda x: ((x['High'].rolling(window=span_b_period).max() + x['Low'].rolling(window=span_b_period).min()) / 2)
    ).shift(span_offset).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', and 'Low' columns
df = ichimoku_span_b(df)

# Display the DataFrame with Senkou Span B values
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Senkou_Span_B']])
