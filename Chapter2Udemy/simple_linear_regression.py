from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv("./DataFolder/SimpleLinearRegression/Salary_Data.csv")

print type(dataset)

#pandas has many ways to select data- loc, iloc, iat
#iloc- choose rows by index but slow
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
X = dataset.iloc[:,:-1].values
y= dataset.iloc[:,1].values

print type(X)
print type(y)
print 1/3


#splitting data into training and testing set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3, random_state=0)

# #feature scaling
# from sklearn.preprocessing import StandardScaler
# sc_X= StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# #fit is not needed
# X_test = sc_X.transform(X_test)

#fit simple linear regression to the training set
from sklearn.linear_model import  LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

#Visualizing the training set details
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Salary Vs Experience(Training set)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

#Visualizing the testing set details
plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Salary Vs Experience(Testing set)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

print "a"