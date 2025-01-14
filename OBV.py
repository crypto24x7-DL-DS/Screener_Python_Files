import pandas as pd

def obv(df):
    """
    Calculate the On-Balance Volume (OBV) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'Close', and 'Volume' columns.

    Returns:
    DataFrame: Input DataFrame with an added 'OBV' column.
    """
    def calc_obv(group):
        # Initialize OBV with 0
        obv = [0]

        # Calculate OBV values for the group
        for i in range(1, len(group)):
            if group['Close'].iloc[i] > group['Close'].iloc[i - 1]:
                obv.append(obv[-1] + group['Volume'].iloc[i])
            elif group['Close'].iloc[i] < group['Close'].iloc[i - 1]:
                obv.append(obv[-1] - group['Volume'].iloc[i])
            else:
                obv.append(obv[-1])

        # Add OBV column to the group DataFrame
        group['OBV'] = pd.Series(obv, index=group.index)
        return group

    # Group by Symbol and apply the calculation
    df = df.groupby('Symbol', group_keys=False).apply(calc_obv)
    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'Close', and 'Volume' columns
df = obv(df)

# Display the DataFrame with OBV values
print(df[['Symbol', 'Timestamp', 'Close', 'Volume', 'OBV']])
