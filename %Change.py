import pandas as pd

def calculate_percentage_change_with_symbol(df, column='Close', periods=1):
    """
    Calculate the percentage change over a specified number of periods for a given column,
    handling multiple symbols in the dataset.

    Parameters:
    df (DataFrame): DataFrame with at least the specified column and a 'Symbol' column.
    column (str): The column to calculate the percentage change on (default 'Close').
    periods (int): The number of periods over which to calculate the change (default 1).

    Returns:
    DataFrame: Original DataFrame with an added '%_Change' column.
    """
    def calculate_group_change(group):
        group['%_Change'] = group[column].pct_change(periods=periods) * 100
        return group

    # Apply calculation grouped by 'Symbol'
    df = df.groupby('Symbol', group_keys=False).apply(calculate_group_change)

    return df

# Example usage:
# Assuming 'df' is your DataFrame with columns: 'Timestamp', 'Symbol', 'Close', etc.
df = calculate_percentage_change_with_symbol(df, column='Close', periods=1)

# Display the DataFrame with the % Change column added
print(df[['Timestamp', 'Symbol', 'Close', '%_Change']])
