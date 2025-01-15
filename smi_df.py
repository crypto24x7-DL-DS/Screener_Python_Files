import pandas as pd

def calculate_smi(df, period=14, smoothing_period=3):
    """
    Calculate the Stochastic Momentum Index (SMI %K) for a given DataFrame grouped by 'Symbol'.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns.
    period (int): The look-back period for the highest high and lowest low.
    smoothing_period (int): The period to smooth the SMI %K line.

    Returns:
    DataFrame: A DataFrame with an additional 'SMI %K' column representing the SMI %K values.
    """
    def calculate_group_smi(group_df):
        # Calculate the midpoint for the high and low
        high_low_midpoint = (group_df['High'].rolling(window=period).max() + group_df['Low'].rolling(window=period).min()) / 2

        # Calculate the difference between close price and midpoint
        close_midpoint_diff = group_df['Close'] - high_low_midpoint

        # Calculate the smoothing factor for the SMI %K
        smi_k = (100 * close_midpoint_diff) / ((group_df['High'].rolling(window=period).max() - group_df['Low'].rolling(window=period).min()) / 2)

        # Smooth the SMI %K using a rolling mean
        group_df['SMI %K'] = smi_k.rolling(window=smoothing_period).mean()

        return group_df[['SMI %K']]

    # Group by 'Symbol' and apply the SMI calculation to each group
    grouped_df = df.groupby('Symbol').apply(calculate_group_smi)

    return grouped_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
smi_df = calculate_smi(df, period=14, smoothing_period=3)

# Display the resulting DataFrame with SMI %K values for each Symbol
print(smi_df)
