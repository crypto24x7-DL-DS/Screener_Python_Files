import pandas as pd
import numpy as np

def calculate_supertrend(df, atr_period=10, multiplier=3):
    """
    Calculate the Supertrend indicator for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', 'Close' columns.
    atr_period (int): The period for calculating the Average True Range (ATR), default is 10.
    multiplier (float): The multiplier for the ATR, default is 3.

    Returns:
    DataFrame: DataFrame with Supertrend values and direction.
    """

    # Group by Symbol and calculate ATR for each group
    df['TR'] = np.maximum((df['High'] - df['Low']),
                          np.maximum(abs(df['High'] - df['Close'].shift(1)),
                                     abs(df['Low'] - df['Close'].shift(1))))
    df['ATR'] = df.groupby('Symbol')['TR'].rolling(atr_period).mean().reset_index(level=0, drop=True)

    # Calculate Upper and Lower Bands for each group (Symbol)
    df['Upper_Band'] = (df['High'] + df['Low']) / 2 + (multiplier * df['ATR'])
    df['Lower_Band'] = (df['High'] + df['Low']) / 2 - (multiplier * df['ATR'])

    # Initialize Supertrend column
    df['Supertrend'] = np.nan  # Mark as NaN for easier adjustments

    # Supertrend Calculation for each Symbol
    for symbol in df['Symbol'].unique():
        symbol_df = df[df['Symbol'] == symbol]
        for current in range(1, len(symbol_df)):
            if symbol_df['Close'].iloc[current] > symbol_df['Upper_Band'].iloc[current - 1]:
                df.loc[symbol_df.index[current], 'Supertrend'] = symbol_df['Lower_Band'].iloc[current]
            elif symbol_df['Close'].iloc[current] < symbol_df['Lower_Band'].iloc[current - 1]:
                df.loc[symbol_df.index[current], 'Supertrend'] = symbol_df['Upper_Band'].iloc[current]
            else:
                df.loc[symbol_df.index[current], 'Supertrend'] = df.loc[symbol_df.index[current - 1], 'Supertrend']

    # Supertrend Direction
    df['Direction'] = np.where(df['Close'] > df['Supertrend'], 'Uptrend', 'Downtrend')

    # Clean up auxiliary columns if needed
    df.drop(['TR', 'ATR', 'Upper_Band', 'Lower_Band'], axis=1, inplace=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
df = calculate_supertrend(df)

# Display the DataFrame with Supertrend values and direction
print(df[['Timestamp', 'Symbol', 'Close', 'Supertrend', 'Direction']])
