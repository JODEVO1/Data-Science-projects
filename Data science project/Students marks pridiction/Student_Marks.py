# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:22:27 2022

@author: Hp
"""

import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data= pd.read_csv("Student_Marks.CSV")
print(data.head())

# Checking for number of null values
print(data.isnull().sum())

# Checking for the number of values in the number 
# of courses column.

data["number_courses"].value_counts()


# Using scatter plot to check if the number of courses
# affect the marks of the student

figure = px.scatter(data_frame=data, x="number_courses",
                    y = "Marks", size="time_study", 
                    title="Number of cour/ses and Marks Scored" )
figure.show()

# Having seen that the number of courses 
# may not affect the mark of the student;
# let's check the effect of the time of study
# with the marks

figure2 = px.scatter(data_frame = data, x = "time_study",
                     y = "Marks", size="number_courses",
                     title= "Time spent amd Marks Scored",
                     trendline="ols")
figure2.show()

# Having seen that there is a linear relationship between
# the time studied and the marks obtained; let's take a 
# look at the correlation between the marks scored by the 
# students and the two other columns in the data:

correlation = data.corr()
    
print(correlation["Marks"].sort_values(ascending = False))

# The time study column correlates than the other column


# Moving to train the data to predict the mark of a student 

# Splitting the data into training and test sets:
    
    
x = np.array(data[["time_study","number_courses"]])
y = np.array(data["Marks"])
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2,
                                                random_state=0)

# Training the model using Linear regression algorithm

model = LinearRegression()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)

# Now testing the model by giving inputs based on the features we have 
# used to train.

# pridict the mark of student:
    
# Features = [["time_study", "number_courses"]]
features = np.array([[4.508, 3]])
model.predict(features)