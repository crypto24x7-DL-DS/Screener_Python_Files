import pandas as pd

def calculate_vwap_with_symbol(df):
    """
    Calculate the Volume-Weighted Average Price (VWAP) for each symbol in the dataset.
    Resets calculations when the 'Symbol' changes.

    Parameters:
    df (DataFrame): DataFrame with 'Symbol', 'Close', and 'Volume' columns.

    Returns:
    DataFrame: Original DataFrame with an added 'VWAP' column.
    """
    def calculate_vwap_group(group):
        # Calculate cumulative volume * price and cumulative volume
        group['CumVolumePrice'] = (group['Close'] * group['Volume']).cumsum()
        group['CumVolume'] = group['Volume'].cumsum()

        # Calculate VWAP
        group['VWAP'] = group['CumVolumePrice'] / group['CumVolume']

        # Drop intermediary columns for a cleaner DataFrame
        group = group.drop(columns=['CumVolumePrice', 'CumVolume'])
