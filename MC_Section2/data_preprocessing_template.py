import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("../Data_folder/2/Data.csv")

print type(dataset)

#pandas has many ways to select data- loc, iloc, iat
#iloc- choose rows by index but slow
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
X = dataset.iloc[:,:-1].values
y= dataset.iloc[:,3].values

print type(X)
print type(y)

#for missing data/ can be replaced by mean, median or most repeated item based on the context
#scikit library, install scipy
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

#categorizing data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lableEncoder_X = LabelEncoder()
X[:,0] = lableEncoder_X.fit_transform(X[:,0])
onehotEncoder_X = OneHotEncoder(categorical_features=[0])
X = onehotEncoder_X.fit_transform(X).toarray()
lableEncoder_y = LabelEncoder()
y = lableEncoder_X.fit_transform(y)

#splitting data into training and testing set


print "a"