import pandas as pd
import numpy as np

def calculate_wavetrend_momentum(df, length=9, signal_length=3):
    """
    Calculate the WaveTrend Momentum for each Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low' columns.
    length (int): The length for calculating the WaveTrend oscillator.
    signal_length (int): The length for calculating the signal line (optional).

    Returns:
    DataFrame: A DataFrame with 'Symbol', 'WaveTrend', 'WaveTrend_Momentum' columns.
    """
    # Group by Symbol and apply the calculation for each group
    def compute_wavetrend_momentum(group):
        # Step 1: Calculate the typical price (average of High and Low)
        group['AvgPrice'] = (group['High'] + group['Low']) / 2

        # Step 2: Calculate the smoothed average price (SMMA)
        group['SmoothedAvgPrice'] = group['AvgPrice'].rolling(window=length, min_periods=1).mean()

        # Step 3: Calculate the WaveTrend (difference between smoothed Avg Price and the previous value)
        group['WaveTrend'] = group['SmoothedAvgPrice'] - group['SmoothedAvgPrice'].shift(1)

        # Step 4: Calculate the WaveTrend Momentum (rate of change of WaveTrend)
        group['WaveTrend_Momentum'] = group['WaveTrend'] - group['WaveTrend'].shift(1)

        return group[['Symbol', 'WaveTrend', 'WaveTrend_Momentum']]

    # Apply the computation for each Symbol group
    result_df = df.groupby('Symbol').apply(compute_wavetrend_momentum)

    return result_df

# Example usage:
# Assuming 'df' is your DataFrame containing 'Symbol', 'High', 'Low' columns
# df = pd.DataFrame(...)  # Example DataFrame with data
wavetrend_momentum_df = calculate_wavetrend_momentum(df, length=9, signal_length=3)

# Display the resulting DataFrame with WaveTrend and WaveTrend Momentum values for each Symbol
print(wavetrend_momentum_df)
