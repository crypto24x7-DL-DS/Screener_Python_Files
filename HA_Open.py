import pandas as pd

def calculate_ha_open_with_symbol(df):
    """
    Calculate the Heikin-Ashi Open for each row, handling multiple symbols.

    Parameters:
    df (DataFrame): DataFrame with columns 'Symbol', 'Open', and 'HA_Close'.

    Returns:
    DataFrame: Original DataFrame with an added 'HA_Open' column.
    """
    def calculate_group_ha_open(group):
        # Initialize the first HA_Open value (same as the first Open for the group)
        ha_open = [group['Open'].iloc[0]]

        # Calculate HA_Open for each row in the group
        for i in range(1, len(group)):
            ha_open.append((ha_open[i-1] + group['HA_Close'].iloc[i-1]) / 2)

        group['HA_Open'] = ha_open
        return group

    # Apply calculation grouped by 'Symbol'
    df = df.groupby('Symbol', group_keys=False).apply(calculate_group_ha_open)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with columns: 'Timestamp', 'Symbol', 'Open', 'HA_Close', etc.
df = calculate_ha_open_with_symbol(df)

# Display the DataFrame with the HA_Open column added
print(df[['Timestamp', 'Symbol', 'Open', 'HA_Close', 'HA_Open']])
