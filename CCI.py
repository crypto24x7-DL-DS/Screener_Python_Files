import pandas as pd

def cci(df, period=20, constant=0.015):
    """
    Calculate the Commodity Channel Index (CCI) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns.
    period (int): Lookback period for the CCI calculation.
    constant (float): Constant scaling factor (usually set to 0.015).

    Returns:
    DataFrame: Input DataFrame with an added 'CCI' column.
    """
    def calc_cci(group):
        # Step 1: Calculate the Typical Price
        tp = (group['High'] + group['Low'] + group['Close']) / 3

        # Step 2: Calculate the Simple Moving Average (SMA) of the Typical Price
        sma_tp = tp.rolling(window=period).mean()

        # Step 3: Calculate the Mean Deviation
        mean_deviation = tp.rolling(window=period).apply(lambda x: pd.Series(x).mad(), raw=True)

        # Step 4: Calculate the CCI
        group['CCI'] = (tp - sma_tp) / (constant * mean_deviation)

        return group

    # Group by Symbol and apply the calculation
    df = df.groupby('Symbol').apply(calc_cci)
    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
df = cci(df)

# Display the DataFrame with CCI values
print(df[['Symbol', 'Timestamp', 'High', 'Low', 'Close', 'CCI']])
