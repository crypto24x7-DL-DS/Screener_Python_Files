def calculate_rsi_with_symbol(df, window_length):
    """
    Calculate RSI for each symbol in the dataset.
    Resets calculations when Symbol changes.
    Args:
        df (pd.DataFrame): DataFrame with 'Symbol' and 'Close' columns.
        window_length (int): Lookback period for RSI calculation.
    Returns:
        pd.DataFrame: DataFrame with 'Symbol', 'RSI', and where the RSI condition is met.
    """
    def rsi_calc(group):
        delta = group['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=window_length, min_periods=1).mean()
        avg_loss = loss.rolling(window=window_length, min_periods=1).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    # Apply calculation grouped by 'Symbol'
    df['RSI'] = df.groupby('Symbol', group_keys=False).apply(rsi_calc)

    # Example: Filter where RSI < 30 and include 'Symbol'
    condition_met = df[df['RSI'] < 60][['Timestamp', 'Symbol', 'RSI']]

    return condition_met

print(df[['Timestamp', 'Close', 'RSI','Symbol']])