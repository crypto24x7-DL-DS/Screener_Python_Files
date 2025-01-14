import pandas as pd

def mfi(df, period=14):
    """
    Calculate the Money Flow Index (MFI) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', 'Close', and 'Volume' columns.
    period (int): Lookback period for the MFI calculation.

    Returns:
    DataFrame: Input DataFrame with an added 'MFI' column.
    """
    def calc_mfi(group):
        # Step 1: Calculate the Typical Price (TP)
        tp = (group['High'] + group['Low'] + group['Close']) / 3

        # Step 2: Calculate the Raw Money Flow (RMF)
        rmf = tp * group['Volume']

        # Step 3: Separate Positive and Negative Money Flow
        positive_flow = rmf.where(tp > tp.shift(1), 0)
        negative_flow = rmf.where(tp < tp.shift(1), 0)

        # Step 4: Calculate the Money Flow Ratio
        money_flow_ratio = positive_flow.rolling(window=period).sum() / negative_flow.rolling(window=period).sum()

        # Step 5: Calculate the Money Flow Index (MFI)
        group['MFI'] = 100 - (100 / (1 + money_flow_ratio))

        return group

    # Group by Symbol and apply the calculation
    df = df.groupby('Symbol').apply(calc_mfi)
    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', 'Close', and 'Volume' columns
df = mfi(df)

# Display the DataFrame with MFI values
print(df[['Symbol', 'Timestamp', 'High', 'Low', 'Close', 'Volume', 'MFI']])
