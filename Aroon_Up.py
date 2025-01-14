import pandas as pd

def calculate_aroon_up(df, lookback_period=25):
    """
    Calculate the Aroon Up indicator for a given DataFrame grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol' and 'High' prices.
    lookback_period (int): The period over which to calculate the Aroon Up (default is 25).

    Returns:
    DataFrame: A DataFrame with an additional 'Aroon_Up' column for each Symbol.
    """
    # Grouping by 'Symbol'
    def aroon_up_for_group(group):
        # Identify the period since the highest high over the lookback period
        group['High_Max_Period'] = group['High'].rolling(window=lookback_period).apply(lambda x: lookback_period - x[::-1].argmax(), raw=True)

        # Calculate the Aroon Up
        group['Aroon_Up'] = ((lookback_period - group['High_Max_Period']) / lookback_period) * 100

        # Drop the intermediate column for clarity
        group.drop(columns=['High_Max_Period'], inplace=True)

        return group[['Symbol', 'Aroon_Up']]

    # Apply the function to each group and combine the results
    result_df = df.groupby('Symbol').apply(aroon_up_for_group).reset_index(drop=True)

    return result_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol' and 'High' columns
aroon_up_df = calculate_aroon_up(df, lookback_period=25)

# Display the resulting DataFrame with Aroon Up values for each Symbol
print(aroon_up_df[['Symbol', 'Aroon_Up']])
