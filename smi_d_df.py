import pandas as pd

def calculate_smi_d(df, period=14, smoothing_k=3, smoothing_d=3):
    """
    Calculate the Stochastic Momentum Index %D (SMI %D) for a given DataFrame grouped by 'Symbol'.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns.
    period (int): The look-back period for calculating highest high and lowest low.
    smoothing_k (int): The smoothing period for SMI %K.
    smoothing_d (int): The smoothing period for SMI %D.

    Returns:
    DataFrame: A DataFrame with additional columns 'SMI %K' and 'SMI %D' for each Symbol.
    """
    def calculate_group_smi_d(group_df):
        # Calculate the midpoint for high and low
        high_low_midpoint = (group_df['High'].rolling(window=period).max() + group_df['Low'].rolling(window=period).min()) / 2

        # Calculate the difference between the close price and the midpoint
        close_midpoint_diff = group_df['Close'] - high_low_midpoint

        # Calculate the SMI %K
        smi_k = (100 * close_midpoint_diff) / ((group_df['High'].rolling(window=period).max() - group_df['Low'].rolling(window=period).min()) / 2)
        smi_k_smoothed = smi_k.rolling(window=smoothing_k).mean()

        # Calculate the SMI %D as a moving average of SMI %K
        group_df['SMI %K'] = smi_k_smoothed
        group_df['SMI %D'] = smi_k_smoothed.rolling(window=smoothing_d).mean()

        return group_df[['SMI %K', 'SMI %D']]

    # Group by 'Symbol' and apply the SMI calculation to each group
    grouped_df = df.groupby('Symbol').apply(calculate_group_smi_d)

    return grouped_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
smi_d_df = calculate_smi_d(df, period=14, smoothing_k=3, smoothing_d=3)

# Display the resulting DataFrame with SMI %K and SMI %D values
print(smi_d_df)
