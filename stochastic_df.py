import pandas as pd

def calculate_slow_stochastic(df, period_k=14, smoothing_k=3, smoothing_d=3):
    """
    Calculate Slow Stochastic %K and Slow Stochastic %D for a given DataFrame grouped by 'Symbol'.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns.
    period_k (int): The look-back period for calculating highest high and lowest low for %K.
    smoothing_k (int): The smoothing period for Slow %K.
    smoothing_d (int): The smoothing period for Slow %D.

    Returns:
    DataFrame: A DataFrame with additional columns 'Slow %K' and 'Slow %D' for each Symbol.
    """
    def calculate_group_stochastic(group_df):
        # Calculate the highest high and lowest low over the period for each group
        high_max = group_df['High'].rolling(window=period_k).max()
        low_min = group_df['Low'].rolling(window=period_k).min()

        # Calculate Fast Stochastic %K
        fast_k = 100 * (group_df['Close'] - low_min) / (high_max - low_min)

        # Smooth Fast %K to get Slow %K
        slow_k = fast_k.rolling(window=smoothing_k).mean()

        # Smooth Slow %K to get Slow %D
        slow_d = slow_k.rolling(window=smoothing_d).mean()

        group_df['Slow %K'] = slow_k
        group_df['Slow %D'] = slow_d

        return group_df[['Slow %K', 'Slow %D']]

    # Group by 'Symbol' and apply the stochastic calculation to each group
    grouped_df = df.groupby('Symbol').apply(calculate_group_stochastic)

    return grouped_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
stochastic_df = calculate_slow_stochastic(df, period_k=14, smoothing_k=3, smoothing_d=3)

# Display the resulting DataFrame with Slow %K and Slow %D values
print(stochastic_df)