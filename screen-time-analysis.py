# Screen Time Analysis Project

import pandas as pd
import numpy as np
# python graphing library
import plotly.express as px
import plotly.graph_objects
import statsmodels
import statsmodels.formula.api as smf

# load CSV
data = pd.read_csv("Screentime-App-Details.csv")
# get the first 5 rows of the dataset
print("\nQuick overview of the dataframe:")
print(data.head())

# check for null values in the dataset
print("\nCheck for null values:")
print(data.isnull().sum())

# analyze/summarize data
print("\nSummarize data:")
print(data.describe())

# create bar chart with usage
figure = px.bar(
    data_frame=data,
    x="Date", # name of a column in the dataframe whose values are used to position marks along the x-axis.
    y="Usage", # name of a column in the dataframe whose values are used to position marks along the y-axis.
    color="App", # name of a column used to assign color to marks.
    title="Usage Per Day" # bar graph title
)
# show bar graph
figure.show()

# create bar chart with notifications
figure = px.bar(
    data_frame=data,
    x="Date", # name of a column in the dataframe whose values are used to position marks along the x-axis.
    y="Notifications", # name of a column in the dataframe whose values are used to position marks along the y-axis.
    color="App", # name of a column used to assign color to marks
    title="Notifications Per Day" # bar graph title
)
# show bar graph
figure.show()

# create bar chart with number of times apps opened
figure = px.bar(
    data_frame=data,
    x="Date", # name of a column in the dataframe whose values are used to position marks along the x-axis.
    y="Times opened", # name of a column in the dataframe whose values are used to position marks along the y-axis.
    color="App", # name of a column used to assign color to marks
    title="Times Opened Per Day" # bar graph title
)
# show bar graph
figure.show()

# create scatter plot with notifications and number of times apps opened
figure = px.scatter(
    data_frame=data,
    x="Notifications", # name of a column in the dataframe whose values are used to position marks along the x-axis.
    y="Usage", # name of a column in the dataframe whose values are used to position marks along the y-axis.
    size="Notifications", # name of a column in the dataframe whose values are used to assign mark sizes.
    trendline="ols", # Draw an ordinary least squares regression line
    title="Relationship Between Number of Notifications and App Usage" # scatter plot title
)
# Show scatter plot
figure.show()

# Least Squares Regression Summary
model = smf.ols('Notifications ~ Usage', data=data)
results = model.fit()
print(results.summary())

