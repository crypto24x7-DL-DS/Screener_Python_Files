def calculate_rma(df, window):
    """
    Calculate the Rolling Moving Average (RMA) for a specified window, separately for each symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Close'].
    window (int): The window length for calculating the RMA.

    Returns:
    DataFrame: Original DataFrame with a new RMA column calculated separately for each symbol.
    """
    # Group by 'Symbol' and calculate RMA for each group
    def rma_group(group):
        sma = group['Close'].rolling(window=window).mean()
        rma = pd.Series(index=group.index, dtype='float64')
        rma[window-1] = sma[window-1]  # Set the first full SMA as the starting RMA
        for i in range(window, len(group)):
            rma[i] = (rma[i-1] * (window - 1) + group['Close'].iloc[i]) / window
        return rma

    # Apply RMA calculation for each group
    df[f'RMA_{window}'] = df.groupby('Symbol', group_keys=False).apply(rma_group)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with at least 'Symbol' and 'Close' columns
df = calculate_rma(df, 14)  # For a 14-period RMA

# Display the DataFrame with RMA values and Symbol column
print(df[['Symbol', 'Timestamp', 'Close', f'RMA_14']])
