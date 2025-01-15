import numpy as np
import pandas as pd

# Function for Bracket (Returns the input value as-is)
def bracket(value):
    return value

# Function for Min (Returns the minimum value within a specified duration)
def min_duration(df, column, duration):
    return df[column].rolling(window=duration).min()

# Function for Max (Returns the maximum value within a specified duration)
def max_duration(df, column, duration):
    return df[column].rolling(window=duration).max()

# Function for Greatest (Returns the greatest value among multiple fields)
def greatest(*args):
    return max(args)

# Function for Least (Returns the smallest value among multiple fields)
def least(*args):
    return min(args)

# Function for Count (Counts occurrences within a duration based on a filter)
def count(df, column, duration, condition):
    return df[column].rolling(window=duration).apply(lambda x: sum(condition(x)), raw=False)

# Function for Countstreak (Counts consecutive occurrences based on filter)
def countstreak(df, column, duration, condition):
    streak_count = (df[column].apply(condition) != 0).astype(int).groupby((df[column].apply(condition) == 0).cumsum()).cumcount() + 1
    return streak_count.rolling(window=duration).max()

# Function for Absolute Value (Abs)
def abs_value(value):
    return abs(value)

# Function for Ceiling Value (Ceil)
def ceil_value(value):
    return np.ceil(value)

# Function for Floor Value (Floor)
def floor_value(value):
    return np.floor(value)

# Function for Rounding Value (Round)
def round_value(value, decimals=0):
    return round(value, decimals)

# Function for Square
def square(value):
    return value ** 2

# Function for Square Root
def square_root(value):
    return np.sqrt(value)

# Function for Natural Logarithm (Log)
def log(value):
    return np.log(value)

# Function for Logarithm Base 10 (Log10)
def log10(value):
    return np.log10(value)
