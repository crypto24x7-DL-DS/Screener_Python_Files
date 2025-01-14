import pandas as pd

def ichimoku_cloud_bottom(df, span_b_period=52, span_offset=26):
    """
    Calculate the Ichimoku Cloud Bottom (Senkou Span B) for a given DataFrame, grouped by 'Symbol'.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', and 'Symbol' columns.
    span_b_period (int): The period for calculating Senkou Span B, default is 52.
    span_offset (int): The period to shift Cloud Bottom forward, typically 26.

    Returns:
    DataFrame: A DataFrame with the Cloud Bottom (Senkou Span B) for each Symbol.
    """
    # Group by 'Symbol'
    def calculate_cloud_bottom(symbol_df):
        # Cloud Bottom (Senkou Span B)
        cloud_bottom = ((symbol_df['High'].rolling(window=span_b_period).max() +
                         symbol_df['Low'].rolling(window=span_b_period).min()) / 2).shift(span_offset)

        # Add Cloud Bottom to the DataFrame
        symbol_df['Cloud_Bottom'] = cloud_bottom

        return symbol_df

    # Apply the function to each group (grouped by 'Symbol')
    df = df.groupby('Symbol').apply(calculate_cloud_bottom)

    return df[['Timestamp', 'Symbol', 'High', 'Low', 'Cloud_Bottom']]

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low' columns
df = ichimoku_cloud_bottom(df)

# Display the DataFrame with Cloud Bottom
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Cloud_Bottom']])
