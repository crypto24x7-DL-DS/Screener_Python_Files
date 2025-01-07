import pandas as pd

def calculate_moving_average_with_symbol(df, window_length):
    """
    Calculate the moving average (MA) for each symbol in the dataset.
    Resets calculations when the 'Symbol' changes.

    Parameters:
    df (DataFrame): DataFrame with 'Symbol' and 'Close' columns.
    window_length (int): The look-back period for the moving average calculation (e.g., 50 for a 50-day MA).

    Returns:
    DataFrame: Original DataFrame with an added 'MA_{window_length}' column.
    """
    def calculate_ma(group):
        group[f'MA_{window_length}'] = group['Close'].rolling(window=window_length).mean()
        return group

    # Apply calculation grouped by 'Symbol'
    df = df.groupby('Symbol', group_keys=False).apply(calculate_ma)

    # Return the DataFrame with the calculated moving average
    return df

# Example usage:
# Assuming 'df' is your DataFrame with columns: 'Timestamp', 'Close', 'Symbol', etc.
window_length = 50  # e.g., a 50-day moving average
df = calculate_moving_average_with_symbol(df, window_length)

# Display the DataFrame with the moving average column added
print(df[['Timestamp', 'Symbol', 'Close', f'MA_{window_length}']])
