import numpy as np

def calculate_hma(df, window):
    """
    Calculate the Hull Moving Average (HMA) for a specified window, separately for each symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Close'].
    window (int): The window length for calculating the HMA.

    Returns:
    DataFrame: Original DataFrame with a new HMA column calculated separately for each symbol.
    """
    # Group by 'Symbol' and calculate HMA for each group
    def hma_group(group):
        # Step 1: Calculate the weighted moving average (WMA) for half of the window length
        half_window = int(window / 2)
        wma_half = group['Close'].rolling(window=half_window).apply(
            lambda x: np.dot(x, np.arange(1, half_window + 1)) / half_window, raw=True
        )

        # Step 2: Calculate the WMA for the full window length
        wma_full = group['Close'].rolling(window=window).apply(
            lambda x: np.dot(x, np.arange(1, window + 1)) / window, raw=True
        )

        # Step 3: Calculate the Hull Moving Average (HMA) by using the two WMAs
        hma_raw = 2 * wma_half - wma_full

        # Step 4: Smooth the HMA using WMA with the square root of the window length
        hma_window = int(np.sqrt(window))
        hma = hma_raw.rolling(window=hma_window).apply(
            lambda x: np.dot(x, np.arange(1, hma_window + 1)) / hma_window, raw=True
        )

        return hma

    # Apply HMA calculation for each symbol group
    df[f'HMA_{window}'] = df.groupby('Symbol', group_keys=False).apply(hma_group)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with at least 'Symbol' and 'Close' columns
df = calculate_hma(df, 20)  # For a 20-period HMA

# Display the DataFrame with HMA values and Symbol column
print(df[['Symbol', 'Timestamp', 'Close', f'HMA_{20}']])
