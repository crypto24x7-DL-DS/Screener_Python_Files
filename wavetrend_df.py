import pandas as pd
import numpy as np

def calculate_wavetrend(df, length=9, signal_length=3):
    """
    Calculate WaveTrend oscillator and its signal line for each Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', and 'Low' columns.
    length (int): The length for calculating the WaveTrend oscillator.
    signal_length (int): The length for calculating the signal line.

    Returns:
    DataFrame: A DataFrame with 'Symbol', 'WaveTrend' and 'Signal_Line' columns.
    """
    # Group by Symbol and apply the calculation for each group
    def compute_wavetrend(group):
        # Step 1: Calculate the average price (typical price)
        group['AvgPrice'] = (group['High'] + group['Low']) / 2

        # Step 2: Calculate the smoothed average price (SMMA)
        group['SmoothedAvgPrice'] = group['AvgPrice'].rolling(window=length, min_periods=1).mean()

        # Step 3: Calculate the WaveTrend (difference between smoothed Avg Price and the previous value)
        group['WaveTrend'] = group['SmoothedAvgPrice'] - group['SmoothedAvgPrice'].shift(1)

        # Step 4: Calculate the signal line as the smoothed WaveTrend
        group['Signal_Line'] = group['WaveTrend'].rolling(window=signal_length).mean()

        return group[['Symbol', 'WaveTrend', 'Signal_Line']]

    # Apply the computation for each Symbol group
    result_df = df.groupby('Symbol').apply(compute_wavetrend)

    return result_df

# Example usage:
# Assuming 'df' is your DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns
# df = pd.DataFrame(...)  # Example DataFrame with data
wavetrend_df = calculate_wavetrend(df, length=9, signal_length=3)

# Display the resulting DataFrame with WaveTrend and Signal Line values for each Symbol
print(wavetrend_df)
