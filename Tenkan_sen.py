import pandas as pd

def ichimoku_conversion_line(df, period=9):
    """
    Calculate the Ichimoku Conversion Line (Tenkan-sen) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', and 'Low' columns.
    period (int): The period over which to calculate the Conversion Line, default is 9.

    Returns:
    DataFrame: DataFrame with the calculated Tenkan-sen for each Symbol.
    """
    # Group by Symbol and calculate the Tenkan-sen (Conversion Line) for each group
    df['Tenkan_sen'] = df.groupby('Symbol').apply(
        lambda x: (x['High'].rolling(window=period).max() + x['Low'].rolling(window=period).min()) / 2
    ).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', and 'Low' columns
df = ichimoku_conversion_line(df)

# Display the DataFrame with Tenkan-sen values
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Tenkan_sen']])
