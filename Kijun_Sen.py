import pandas as pd

def ichimoku_base_line(df, period=26):
    """
    Calculate the Ichimoku Base Line (Kijun-sen) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', and 'Low' columns.
    period (int): The period over which to calculate the Base Line, default is 26.

    Returns:
    DataFrame: DataFrame with the calculated Kijun-sen for each Symbol.
    """
    # Group by Symbol and calculate the Kijun-sen (Base Line) for each group
    df['Kijun_sen'] = df.groupby('Symbol').apply(
        lambda x: (x['High'].rolling(window=period).max() + x['Low'].rolling(window=period).min()) / 2
    ).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', and 'Low' columns
df = ichimoku_base_line(df)

# Display the DataFrame with Kijun-sen values
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Kijun_sen']])
