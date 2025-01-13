def calculate_tema(df, window):
    """
    Calculate the Triple Exponential Moving Average (TEMA) for a specified window, separately for each symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Close'].
    window (int): The window length for calculating the TEMA.

    Returns:
    DataFrame: Original DataFrame with a new TEMA column calculated separately for each symbol.
    """
    # Group by 'Symbol' and calculate TEMA for each group
    def tema_group(group):
        # First EMA
        ema1 = group['Close'].ewm(span=window, adjust=False).mean()
        # Second EMA on the first EMA
        ema2 = ema1.ewm(span=window, adjust=False).mean()
        # Third EMA on the second EMA
        ema3 = ema2.ewm(span=window, adjust=False).mean()
        # Calculate TEMA
        tema = (3 * ema1) - (3 * ema2) + ema3
        return tema

    # Apply TEMA calculation for each group
    df[f'TEMA_{window}'] = df.groupby('Symbol', group_keys=False).apply(tema_group)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with at least 'Symbol' and 'Close' columns
df = calculate_tema(df, 14)  # For a 14-period TEMA

# Display the DataFrame with TEMA values and Symbol column
print(df[['Symbol', 'Timestamp', 'Close', f'TEMA_14']])
