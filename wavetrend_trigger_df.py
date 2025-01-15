import pandas as pd
import numpy as np

def calculate_wavetrend_trigger(df, length=9, signal_length=3, threshold=0):
    """
    Calculate the WaveTrend oscillator and its trigger signal for each Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns.
    length (int): The length for calculating the WaveTrend oscillator.
    signal_length (int): The length for calculating the signal line.
    threshold (float): The value of the threshold for triggering the signal (default is 0).

    Returns:
    DataFrame: A DataFrame with 'Symbol', 'WaveTrend', 'Signal_Line', and 'WaveTrend_Trigger' columns.
    """
    # Group by Symbol and apply the calculation for each group
    def compute_wavetrend_trigger(group):
        # Step 1: Calculate the average price (typical price)
        group['AvgPrice'] = (group['High'] + group['Low']) / 2

        # Step 2: Calculate the smoothed average price (SMMA)
        group['SmoothedAvgPrice'] = group['AvgPrice'].rolling(window=length, min_periods=1).mean()

        # Step 3: Calculate the WaveTrend (difference between smoothed Avg Price and the previous value)
        group['WaveTrend'] = group['SmoothedAvgPrice'] - group['SmoothedAvgPrice'].shift(1)

        # Step 4: Calculate the signal line as the smoothed WaveTrend
        group['Signal_Line'] = group['WaveTrend'].rolling(window=signal_length).mean()

        # Step 5: Generate the WaveTrend Trigger based on the crossing of the threshold
        group['WaveTrend_Trigger'] = np.where(group['WaveTrend'] > threshold, 1, 0)  # 1 for above threshold, 0 for below

        return group[['Symbol', 'WaveTrend', 'Signal_Line', 'WaveTrend_Trigger']]

    # Apply the computation for each Symbol group
    result_df = df.groupby('Symbol').apply(compute_wavetrend_trigger)

    return result_df

# Example usage:
# Assuming 'df' is your DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns
# df = pd.DataFrame(...)  # Example DataFrame with data
wavetrend_trigger_df = calculate_wavetrend_trigger(df, length=9, signal_length=3, threshold=0)

# Display the resulting DataFrame with WaveTrend, Signal Line, and Trigger signal values for each Symbol
print(wavetrend_trigger_df)
