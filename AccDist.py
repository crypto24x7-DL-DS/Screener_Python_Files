import pandas as pd

def accumulation_distribution(df):
    """
    Calculate the Accumulation/Distribution (AccDist) Line for a given DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', 'Close', and 'Volume' columns.

    Returns:
    DataFrame: The input DataFrame with an added 'AccDist' column.
    """
    def calc_acc_dist(group):
        # Money Flow Multiplier
        money_flow_multiplier = ((group['Close'] - group['Low']) - (group['High'] - group['Close'])) / (group['High'] - group['Low'])

        # Handle cases where High equals Low to avoid division by zero
        money_flow_multiplier = money_flow_multiplier.fillna(0)

        # Money Flow Volume
        money_flow_volume = money_flow_multiplier * group['Volume']

        # Accumulation/Distribution Line (ADL)
        acc_dist_line = money_flow_volume.cumsum()

        # Add ADL to the group DataFrame
        group['AccDist'] = acc_dist_line
        return group

    # Group by Symbol and apply the calculation
    df = df.groupby('Symbol').apply(calc_acc_dist)
    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', 'Close', and 'Volume' columns
df = accumulation_distribution(df)

# Display the DataFrame with AccDist values
print(df[['Symbol', 'Timestamp', 'High', 'Low', 'Close', 'Volume', 'AccDist']])
