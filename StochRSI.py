import pandas as pd

def stoch_rsi(df, rsi_period=14, stoch_period=14):
    """
    Calculate the Stochastic RSI (StochRSI) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol' and 'Close' columns.
    rsi_period (int): Lookback period for the RSI calculation.
    stoch_period (int): Lookback period for the StochRSI calculation.

    Returns:
    DataFrame: Input DataFrame with an added 'StochRSI' column.
    """
    def calc_stoch_rsi(group):
        # Step 1: Calculate the RSI
        delta = group['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        # Step 2: Calculate the Stochastic Oscillator of the RSI values
        min_rsi = rsi.rolling(window=stoch_period).min()
        max_rsi = rsi.rolling(window=stoch_period).max()
        group['StochRSI'] = (rsi - min_rsi) / (max_rsi - min_rsi)

        # Handling NaN values if any
        group['StochRSI'] = group['StochRSI'].fillna(0)

        return group

    # Group by Symbol and apply the calculation
    df = df.groupby('Symbol').apply(calc_stoch_rsi)
    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol' and 'Close' columns
df = stoch_rsi(df)

# Display the DataFrame with StochRSI values
print(df[['Symbol', 'Timestamp', 'Close', 'StochRSI']])
