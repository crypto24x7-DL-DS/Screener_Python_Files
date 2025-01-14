import pandas as pd

def cmf(df, period=20):
    """
    Calculate the Chaikin Money Flow (CMF) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', 'Close', and 'Volume' columns.
    period (int): Lookback period for the CMF calculation.

    Returns:
    DataFrame: Input DataFrame with an added 'CMF' column.
    """
    def calc_cmf(group):
        # Step 1: Calculate the Money Flow Multiplier
        mfm = ((group['Close'] - group['Low']) - (group['High'] - group['Close'])) / (group['High'] - group['Low'])
        mfm = mfm.fillna(0)  # Handle division by zero cases

        # Step 2: Calculate the Money Flow Volume
        mfv = mfm * group['Volume']

        # Step 3: Calculate the CMF
        group['CMF'] = mfv.rolling(window=period).sum() / group['Volume'].rolling(window=period).sum()

        return group

    # Group by Symbol and apply the calculation
    df = df.groupby('Symbol').apply(calc_cmf)
    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', 'Close', and 'Volume' columns
df = cmf(df)

# Display the DataFrame with CMF values
print(df[['Symbol', 'Timestamp', 'High', 'Low', 'Close', 'Volume', 'CMF']])
