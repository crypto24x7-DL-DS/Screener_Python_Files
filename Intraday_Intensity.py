import pandas as pd

def intraday_intensity(df):
    """
    Calculate the Intraday Intensity (II) for a given DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', 'Close', 'Volume', and 'Symbol' columns.

    Returns:
    DataFrame: The DataFrame with Intraday Intensity values for each Symbol group.
    """
    # Group by 'Symbol' and apply the Intraday Intensity calculation for each group
    def calculate_intraday_intensity(group):
        # Calculate Intraday Intensity
        ii = ((group['Close'] - group['Low']) - (group['High'] - group['Close'])) / (group['High'] - group['Low']) * group['Volume']
        return ii

    # Apply the function to each group
    df['Intraday_Intensity'] = df.groupby('Symbol').apply(calculate_intraday_intensity).reset_index(level=0, drop=True)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'High', 'Low', 'Close', 'Volume', and 'Symbol' columns
df['Intraday_Intensity'] = intraday_intensity(df)

# Display the DataFrame with Intraday Intensity values
print(df[['Timestamp', 'Symbol', 'High', 'Low', 'Close', 'Volume', 'Intraday_Intensity']])
