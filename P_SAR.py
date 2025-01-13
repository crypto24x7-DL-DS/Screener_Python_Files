def calculate_parabolic_sar(df, initial_af=0.02, max_af=0.2):
    """
    Calculate the Parabolic SAR for each row in the DataFrame, grouped by Symbol.

    Parameters:
    df (DataFrame): DataFrame containing 'Symbol', 'High', 'Low', 'Close' columns.
    initial_af (float): The initial acceleration factor, default is 0.02.
    max_af (float): The maximum acceleration factor, default is 0.2.

    Returns:
    DataFrame: DataFrame with calculated Parabolic SAR values.
    """
    # Initialize columns for SAR, Acceleration Factor (AF), Extreme Point (EP), and Trend
    df['SAR'] = 0.0
    df['AF'] = initial_af
    df['EP'] = 0.0  # Extreme point (EP) starts as 0
    df['trend'] = 1  # 1 for uptrend, -1 for downtrend

    # Grouping by 'Symbol' and applying the SAR calculation to each group
    for symbol, group in df.groupby('Symbol'):
        # Loop through each row in the group (group is now a subset of the original DataFrame for each symbol)
        for i in range(1, len(group)):
            if group['trend'].iloc[i-1] == 1:  # Uptrend
                group.at[i, 'EP'] = max(group.at[i-1, 'EP'], group.at[i, 'High'])
                group.at[i, 'SAR'] = group.at[i-1, 'SAR'] + group.at[i-1, 'AF'] * (group.at[i-1, 'EP'] - group.at[i-1, 'SAR'])

                if group.at[i, 'SAR'] > group.at[i, 'Low']:
                    group.at[i, 'SAR'] = group.at[i, 'Low']
                    group.at[i, 'trend'] = -1
                    group.at[i, 'AF'] = initial_af  # Reset AF for downtrend
                    group.at[i, 'EP'] = group.at[i, 'Low']  # Set EP to the lowest price in the downtrend
            else:  # Downtrend
                group.at[i, 'EP'] = min(group.at[i-1, 'EP'], group.at[i, 'Low'])
                group.at[i, 'SAR'] = group.at[i-1, 'SAR'] + group.at[i-1, 'AF'] * (group.at[i-1, 'SAR'] - group.at[i-1, 'EP'])

                if group.at[i, 'SAR'] < group.at[i, 'High']:
                    group.at[i, 'SAR'] = group.at[i, 'High']
                    group.at[i, 'trend'] = 1
                    group.at[i, 'AF'] = min(group.at[i-1, 'AF'] + initial_af, max_af)  # Increase AF
                    group.at[i, 'EP'] = group.at[i, 'High']  # Set EP to the highest price in the uptrend

        # After processing the group, assign the updated group back to the main DataFrame
        df.loc[group.index, ['SAR', 'AF', 'EP', 'trend']] = group[['SAR', 'AF', 'EP', 'trend']]

    return df

# Example usage:
# Assuming 'df' is your DataFrame with 'Symbol', 'High', 'Low', 'Close' columns
df = calculate_parabolic_sar(df)

# Display the DataFrame with Parabolic SAR
print(df[['Symbol', 'Timestamp', 'High', 'Low', 'Close', 'SAR']])
