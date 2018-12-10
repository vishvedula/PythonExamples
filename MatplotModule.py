#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas

# Read in the data.
games = pandas.read_csv("D:/PERSONAL/TECH_TIPS/PYTHON/games.csv")
# Print the names of the columns in games.
print(games.columns)

# Make a histogram of all the ratings in the average_rating column.
plt.hist(games["average_rating"])

# Show the plot.
plt.show()

