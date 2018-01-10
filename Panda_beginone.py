import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# creating a series using pandas
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# print s


# Create the dates by passing the range
dates = pd.date_range('20130101', periods=6)

# print dates

# Create a dataframe of random numbers
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# print df

# Creating a DataFrame by passing a dict of objects that can be converted to series-like
df2 = pd.DataFrame({"A": 3,
                    "B": pd.Timestamp("20130102"),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

##########################################################################
# VIEWING DATA

# print df2

# print df2.dtypes

# print df2.A

# print df.head()

# print df.head(2)

# print df.tail()

# print df

# print df.index

# print df2.index

# print df.columns

# print df.values

# print df.describe()

# print df.T

# Doesn't work in old version
# print df.sort_index(axis=1, ascending=False)

# print df.sort_values(by='B')

##########################################################################
# DATA SELECTION:

# print df['A']

# slicing rows
# print df[0:3]
# print df['20130102':'20130104']


##########################################################################
# Selection by labels/indexes:

# print df.loc[dates[0]]
# print df.loc[:,['A','B']]

# print df.loc['20130102':'20130104',['A','B']]

# reduction of the dimension of the returned objects
# df.loc['20130102',['A','B']]

# getting scalar value
# print df.loc[dates[0],'A']

# getting fast access to a scalar
# print df.at[dates[0],'A']

########################################################################
# Selection by position

# print df.iloc[3]

# print df.iloc[3:5,1:3]

# print df.iloc[[1,2,4],[0,2]]

# print df.iloc[1:3,:]

# slicing column explicitly
# print df.iloc[:,1:3]

# print df.iloc[1,1]

# getting fast access to a scalar
# print df.iat[1,1]

######################################################################
# BOOLEAN INDEXING
#print df[df.A > 0]

#print df[df > 0]
