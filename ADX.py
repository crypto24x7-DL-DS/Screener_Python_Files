import pandas as pd

def calculate_adx(df, period=14):
    """
    Calculate the Average Directional Index (ADX) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', and 'Close' prices, and 'Symbol'.
    period (int): Period length for calculating the ADX (usually 14).

    Returns:
    DataFrame: A Pandas DataFrame with columns for +DI, -DI, DX, and ADX.
    """
    # Group by 'Symbol' and apply the ADX calculation for each group
    def calculate_adx_for_group(group):
        # Calculate True Range (TR)
        group['TR'] = group[['High', 'Low', 'Close']].apply(
            lambda row: max(row['High'] - row['Low'], abs(row['High'] - row['Close']), abs(row['Low'] - row['Close'])),
            axis=1
        )
        group['ATR'] = group['TR'].rolling(window=period).mean()

        # Calculate Directional Movement (DM)
        group['+DM'] = group['High'].diff()
        group['-DM'] = -group['Low'].diff()
        group['+DM'] = group.apply(lambda row: row['+DM'] if row['+DM'] > row['-DM'] and row['+DM'] > 0 else 0, axis=1)
        group['-DM'] = group.apply(lambda row: row['-DM'] if row['-DM'] > row['+DM'] and row['-DM'] > 0 else 0, axis=1)

        # Calculate Smoothed +DI and -DI
        group['+DI'] = 100 * (group['+DM'].rolling(window=period).mean() / group['ATR'])
        group['-DI'] = 100 * (group['-DM'].rolling(window=period).mean() / group['ATR'])

        # Calculate DX (Directional Movement Index)
        group['DX'] = 100 * abs(group['+DI'] - group['-DI']) / (group['+DI'] + group['-DI'])

        # Calculate ADX as the rolling average of DX
        group['ADX'] = group['DX'].rolling(window=period).mean()

        return group[['+DI', '-DI', 'DX', 'ADX']]

    # Apply the function to each group
    df[['+DI', '-DI', 'DX', 'ADX']] = df.groupby('Symbol').apply(calculate_adx_for_group).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'High', 'Low', 'Close', and 'Symbol' columns
df = calculate_adx(df)

# Display the resulting DataFrame with ADX values
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Close', '+DI', '-DI', 'DX', 'ADX']])
