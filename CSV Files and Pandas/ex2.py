#Exercise 2 - Reading the Titanic data
import pandas as pd
# import matplotlib.pyplot as plt
#load the titanic data via url
titanic = pd.read_csv('https://vincentarelbundock.github.io/' + 'Rdatasets/csv/carData/TitanicSurvival.csv')
#DataFrame head method returns 1st 5 rows
print(titanic.head())
#DataFrame tail method returns last 5 rows
print(titanic.tail())
#Customize column names
titanic.columns = ["Name", "Survived", "Sex", "Age", "Class"]

print(titanic.head())

#Use describe for simple data analysis
#describe calculates these statistics only for the numeric columns—in this case, just the age column:
print(titanic.describe())
#The Titanic dataset contains only one numerical data column, so the diagram shows one histogram for the age distribution. 
#For datasets with multiple numerical columns, hist creates a separate histogram for each numerical column.
%matplotlib
histogram = titanic.hist()
