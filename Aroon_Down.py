import pandas as pd

def calculate_aroon_down(df, lookback_period=25):
    """
    Calculate the Aroon Down indicator for a given DataFrame grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol' and 'Low' prices.
    lookback_period (int): The period over which to calculate the Aroon Down (default is 25).

    Returns:
    DataFrame: A DataFrame with an additional 'Aroon_Down' column for each Symbol.
    """
    # Grouping by 'Symbol'
    def aroon_down_for_group(group):
        # Identify the period since the lowest low over the lookback period
        group['Low_Min_Period'] = group['Low'].rolling(window=lookback_period).apply(lambda x: lookback_period - x[::-1].argmin(), raw=True)

        # Calculate the Aroon Down
        group['Aroon_Down'] = ((lookback_period - group['Low_Min_Period']) / lookback_period) * 100

        # Drop the intermediate column for clarity
        group.drop(columns=['Low_Min_Period'], inplace=True)

        return group[['Symbol', 'Aroon_Down']]

    # Apply the function to each group and combine the results
    result_df = df.groupby('Symbol').apply(aroon_down_for_group).reset_index(drop=True)

    return result_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol' and 'Low' columns
aroon_down_df = calculate_aroon_down(df, lookback_period=25)

# Display the resulting DataFrame with Aroon Down values for each Symbol
print(aroon_down_df[['Symbol', 'Aroon_Down']])
