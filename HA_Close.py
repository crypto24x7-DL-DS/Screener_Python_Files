import pandas as pd

# Function to calculate Heikin-Ashi Close
def calculate_ha_close(df, symbol):
    """
    Calculate the Heikin-Ashi Close for each row for a given symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Open', 'High', 'Low', 'Close'].
    symbol (str): The symbol to filter for calculation.

    Returns:
    Series: Heikin-Ashi Close values for the specified symbol.
    """
    filtered_df = df[df['Symbol'] == symbol]
    ha_close = (filtered_df['Open'] + filtered_df['High'] + filtered_df['Low'] + filtered_df['Close']) / 4
    return ha_close

# Function to calculate Heikin-Ashi Open
def calculate_ha_open(df, symbol):
    """
    Calculate the Heikin-Ashi Open for each row for a given symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Open', 'Close', 'HA_Close'].
    symbol (str): The symbol to filter for calculation.

    Returns:
    Series: Heikin-Ashi Open values for the specified symbol.
    """
    filtered_df = df[df['Symbol'] == symbol]
    ha_open = [filtered_df['Open'].iloc[0]]  # Initialize the first HA_Open
    for i in range(1, len(filtered_df)):
        ha_open.append((ha_open[i - 1] + filtered_df['HA_Close'].iloc[i - 1]) / 2)
    return pd.Series(ha_open, index=filtered_df.index)

# Function to calculate Heikin-Ashi High
def calculate_ha_high(df, symbol):
    """
    Calculate the Heikin-Ashi High for each row for a given symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'High', 'HA_Open', 'HA_Close'].
    symbol (str): The symbol to filter for calculation.

    Returns:
    Series: Heikin-Ashi High values for the specified symbol.
    """
    filtered_df = df[df['Symbol'] == symbol]
    ha_high = filtered_df[['High', 'HA_Open', 'HA_Close']].max(axis=1)
    return ha_high

# Function to calculate Heikin-Ashi Low
def calculate_ha_low(df, symbol):
    """
    Calculate the Heikin-Ashi Low for each row for a given symbol.

    Parameters:
    df (DataFrame): DataFrame with columns ['Symbol', 'Low', 'HA_Open', 'HA_Close'].
    symbol (str): The symbol to filter for calculation.

    Returns:
    Series: Heikin-Ashi Low values for the specified symbol.
    """
    filtered_df = df[df['Symbol'] == symbol]
    ha_low = filtered_df[['Low', 'HA_Open', 'HA_Close']].min(axis=1)
    return ha_low

# Example Usage:
# Sample multi-symbol DataFrame

# Perform Heikin-Ashi calculations for 'AAPL'
symbol = 'AAPL'
df['HA_Close'] = calculate_ha_close(df, symbol)
df['HA_Open'] = calculate_ha_open(df, symbol)
df['HA_High'] = calculate_ha_high(df, symbol)
df['HA_Low'] = calculate_ha_low(df, symbol)

# Display results
print(df[df['Symbol'] == symbol][['Timestamp', 'Symbol', 'Open', 'High', 'Low', 'Close', 'HA_Open', 'HA_High', 'HA_Low', 'HA_Close']])
