import pandas as pd

def calculate_true_range(df):
    """
    Calculate the True Range (TR) for a given DataFrame grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' prices.

    Returns:
    DataFrame: A Pandas DataFrame with an additional 'TR' column for True Range.
    """
    # Grouping by 'Symbol'
    def true_range_for_group(group):
        group['Previous Close'] = group['Close'].shift(1)
        group['TR'] = group[['High', 'Low', 'Previous Close']].apply(
            lambda row: max(row['High'] - row['Low'], abs(row['High'] - row['Previous Close']), abs(row['Low'] - row['Previous Close'])),
            axis=1
        )
        group.drop(columns=['Previous Close'], inplace=True)  # Optional: remove the helper column if not needed
        return group[['Symbol', 'TR']]

    # Apply the function to each group and combine the results
    result_df = df.groupby('Symbol').apply(true_range_for_group).reset_index(drop=True)

    return result_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
true_range_df = calculate_true_range(df)

# Display the resulting DataFrame with True Range values for each Symbol
print(true_range_df[['Symbol', 'TR']])
