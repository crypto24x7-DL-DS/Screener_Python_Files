import pandas as pd

def calculate_stochastic(df, k_period=14, d_period=3):
    """
    Calculate the Stochastic Oscillator for a given DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', and 'Close' columns.
    k_period (int): The period for calculating %K (default is 14).
    d_period (int): The period for calculating %D (default is 3).

    Returns:
    DataFrame: A DataFrame with additional '%K' and '%D' columns representing
               the Stochastic Oscillator values.
    """
    # Calculate the %K line
    df['Lowest_Low'] = df['Low'].rolling(window=k_period).min()
    df['Highest_High'] = df['High'].rolling(window=k_period).max()
    df['%K'] = ((df['Close'] - df['Lowest_Low']) / (df['Highest_High'] - df['Lowest_Low'])) * 100

    # Calculate the %D line (3-period SMA of %K)
    df['%D'] = df['%K'].rolling(window=d_period).mean()

    # Drop helper columns
    df.drop(columns=['Lowest_Low', 'Highest_High'], inplace=True)

    return df[['%K', '%D']]

def calculate_stochastic_for_symbol(df, k_period=14, d_period=3):
    """
    Calculate Stochastic Oscillator for each Symbol group in the DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', and 'Close' columns.
    k_period (int): The period for calculating %K (default is 14).
    d_period (int): The period for calculating %D (default is 3).

    Returns:
    DataFrame: A DataFrame with '%K' and '%D' for each Symbol.
    """
    # Group by 'Symbol' and apply the stochastic calculation to each group
    def stochastic_for_group(group):
        group[['%K', '%D']] = calculate_stochastic(group, k_period, d_period)
        return group[['Symbol', '%K', '%D']]

    result_df = df.groupby('Symbol').apply(stochastic_for_group).reset_index(drop=True)
    return result_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', and 'Close' columns
stochastic_df = calculate_stochastic_for_symbol(df, k_period=14, d_period=3)

# Display the resulting DataFrame with Stochastic Oscillator values
print(stochastic_df[['Symbol', '%K', '%D']])
