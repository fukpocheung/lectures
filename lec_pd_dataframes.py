""" lec_pd_dataframes.py

Companion codes for the lecture on Dataframes
"""

import pandas as pd


# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# Business (trading) day counter
#In other words, bday_ser takes the value of 1 on January 2, 2 on January 3, etc...
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

# ----------------------------------------------------------------------------
#   Create two series
# ----------------------------------------------------------------------------

# Series with prices
prc_ser = pd.Series(data=prices, index=dates)

# Series with trading day
bday_ser = pd.Series(data=bday, index=dates)


# ----------------------------------------------------------------------------
#   Create a dataframe
# ----------------------------------------------------------------------------
# Data Frame with close and Bday columns
df  = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})
print(df)


# ----------------------------------------------------------------------------
#   Accessing the indexes in a dataframe
# ----------------------------------------------------------------------------
# The attribute `columns` returns the column index
#print(df.columns)
#print('The type of this index is', type(df.columns))

# We can get the series corresponding to a column index label
#col0 = df['Close']
#print(col0)

# Just like any series, you can access the index using:
#print(col0.index)
#print(type(col0.index))

# In fact, this corresponds to the Dataframe index as well
#print(df.index)
#print(type(df.index))


# ----------------------------------------------------------------------------
#   Modifying columns and indexes
# ----------------------------------------------------------------------------
# Modify columns and indexes
#df.columns = ['A', 'B']
#df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(df)

# Then revert back
#df.columns = ['Close', 'Bday']
#df.index = [
#  '2020-01-02',
#  '2020-01-03',
#  '2020-01-06',
#  '2020-01-07',
#  '2020-01-08',
#  '2020-01-09',
#  '2020-01-10',
#  '2020-01-13',
#  '2020-01-14',
#  '2020-01-15',
#]
#print(df)

# ----------------------------------------------------------------------------
#   Sorting
# ----------------------------------------------------------------------------

# Create a series with an unsorted index
new_ser = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])
print(new_ser)

# This will return 'False'
print(new_ser.is_monotonic_increasing)

# Sort the series based on the index
sorted_ser  = '?'
#print(sorted_ser)

# This will return only the first rows (not the entire series as before)
#x = sorted_ser['a':'b'] # --> only first two rows
#print(x)
# Out:
# a    1
# b    2
# dtype: int64

# `sorted_ser` is sorted so the following will return the intersection between
# the slice and the row labels
#x = sorted_ser['b':'z']
#print(x)
# Out:
# b    2
# c    3
# dtype: int64

# Create a series with an unsorted index
ser_sort_inplace  = '?'

# Sort the series. Note that we are not assigning this function call
# to a new variable.
#ser_sort_inplace.sort_index(inplace=True)
#print(ser_sort_inplace)

# ----------------------------------------------------------------------------
#   Create a dataframe
# ----------------------------------------------------------------------------
# Using the series we created above...

# Data Frame with close and Bday columns
df = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})

print(df)
# Output:
#             Close  Bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
# 2020-01-06   7.00     3
# 2020-01-07   7.10     4
# 2020-01-08   6.86     5
# 2020-01-09   6.95     6
# 2020-01-10   7.00     7
# 2020-01-13   7.02     8
# 2020-01-14   7.11     9
# 2020-01-15   7.04    10