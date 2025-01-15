import pandas as pd

def calculate_aroon_up(df, lookback_period=25):
    df['High_Max_Period'] = df['High'].rolling(window=lookback_period).apply(lambda x: lookback_period - x[::-1].argmax(), raw=True)
    df['Aroon_Up'] = ((lookback_period - df['High_Max_Period']) / lookback_period) * 100
    df.drop(columns=['High_Max_Period'], inplace=True)
    return df['Aroon_Up']

def calculate_aroon_down(df, lookback_period=25):
    df['Low_Min_Period'] = df['Low'].rolling(window=lookback_period).apply(lambda x: lookback_period - x[::-1].argmin(), raw=True)
    df['Aroon_Down'] = ((lookback_period - df['Low_Min_Period']) / lookback_period) * 100
    df.drop(columns=['Low_Min_Period'], inplace=True)
    return df['Aroon_Down']

def calculate_aroon_oscillator(df, lookback_period=25):
    """
    Calculate the Aroon Oscillator for a given DataFrame grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'High', 'Low', and 'Symbol'.
    lookback_period (int): The period over which to calculate Aroon Up and Down (default is 25).

    Returns:
    DataFrame: A DataFrame with an additional 'Aroon_Oscillator' column for each Symbol.
    """
    # Group by 'Symbol'
    def aroon_oscillator_for_group(group):
        # Calculate Aroon Up and Aroon Down
        group['Aroon_Up'] = calculate_aroon_up(group, lookback_period)
        group['Aroon_Down'] = calculate_aroon_down(group, lookback_period)

        # Calculate Aroon Oscillator
        group['Aroon_Oscillator'] = group['Aroon_Up'] - group['Aroon_Down']

        return group[['Symbol', 'Aroon_Oscillator']]

    # Apply the function to each group and combine the results
    result_df = df.groupby('Symbol').apply(aroon_oscillator_for_group).reset_index(drop=True)

    return result_df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', and 'Low' columns
aroon_oscillator_df = calculate_aroon_oscillator(df, lookback_period=25)

# Display the resulting DataFrame with Aroon Oscillator values for each Symbol
print(aroon_oscillator_df[['Symbol', 'Aroon_Oscillator']])
