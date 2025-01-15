import pandas as pd

def calculate_fast_stochastic(df, period_k=14, smoothing_d=3):
    """
    Calculate Fast Stochastic %K and Fast Stochastic %D for a given DataFrame grouped by 'Symbol'.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns.
    period_k (int): The look-back period for calculating highest high and lowest low for %K.
    smoothing_d (int): The smoothing period for Fast %D.

    Returns:
    DataFrame: A DataFrame with additional columns 'Fast %K' and 'Fast %D' for each Symbol.
    """
    def calculate_group_stochastic(group_df):
        # Calculate the highest high and lowest low over the period for each group
        high_max = group_df['High'].rolling(window=period_k).max()
        low_min = group_df['Low'].rolling(window=period_k).min()

        # Calculate Fast %K
        fast_k = 100 * (group_df['Close'] - low_min) / (high_max - low_min)

        # Calculate Fast %D as a moving average of Fast %K
        fast_d = fast_k.rolling(window=smoothing_d).mean()

        group_df['Fast %K'] = fast_k
        group_df['Fast %D'] = fast_d

        return group_df[['Fast %K', 'Fast %D']]

    # Group by 'Symbol' and apply the stochastic calculation to each group
    grouped_df = df.groupby('Symbol').apply(calculate_group_stochastic)

    return grouped_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
fast_stochastic_df = calculate_fast_stochastic(df, period_k=14, smoothing_d=3)

# Display the resulting DataFrame with Fast %K and Fast %D values
print(fast_stochastic_df)
