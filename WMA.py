import numpy as np

def calculate_wma(df, window):
    """
    Calculate the Weighted Moving Average (WMA) for a specified window, separately for each symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Close'].
    window (int): The window length for calculating the WMA.

    Returns:
    DataFrame: Original DataFrame with a new WMA column calculated separately for each symbol.
    """
    weights = np.arange(1, window + 1)  # Create an array of weights [1, 2, ..., window]

    # Group by 'Symbol' and calculate WMA for each group
    df[f'WMA_{window}'] = df.groupby('Symbol')['Close'].transform(
        lambda prices: prices.rolling(window=window).apply(
            lambda x: np.dot(x, weights) / weights.sum(), raw=True
        )
    )
    return df

# Example usage:
# Assuming 'df' is your DataFrame with at least 'Symbol' and 'Close' columns
df = calculate_wma(df, 10)  # For a 10-period WMA
df = calculate_wma(df, 20)  # For a 20-period WMA

# Display the DataFrame with WMA values and Symbol column
print(df[['Symbol', 'Timestamp', 'Close', f'WMA_10', f'WMA_20']])
