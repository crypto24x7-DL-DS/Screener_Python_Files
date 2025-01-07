import pandas as pd

def process_volume_with_symbol(df, window_length=1):
    """
    Process volume data grouped by symbol, including moving average and volume surge calculation.
    Resets calculations when the 'Symbol' changes.

    Parameters:
    df (DataFrame): DataFrame with 'Symbol' and 'Volume' columns.
    window_length (int): The look-back period for volume average calculation.

    Returns:
    DataFrame: Original DataFrame with added 'Volume_MA' and 'Volume_Surge' columns.
    """
    def calculate_volume_metrics(group):
        group['Volume_MA'] = group['Volume'].rolling(window=window_length).mean()
        surge_threshold = 2  # Volume surge is defined as 2x the moving average
        group['Volume_Surge'] = group['Volume'] > (group['Volume_MA'] * surge_threshold)
        return group

    # Apply the calculations grouped by 'Symbol'
    df = df.groupby('Symbol', group_keys=False).apply(calculate_volume_metrics)

    # Filter rows where volume surge occurs, including 'Symbol'
    condition_met = df[df['Volume_Surge']][['Timestamp', 'Symbol', 'Volume', 'Volume_MA', 'Volume_Surge']]

    return condition_met

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol' and 'Volume' columns
window_length = 7  # 7-day moving average for volume
result = process_volume_with_symbol(df, window_length)

# Display the filtered DataFrame where the volume surge condition is met
print(result)
