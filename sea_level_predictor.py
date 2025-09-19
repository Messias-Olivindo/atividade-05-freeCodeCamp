import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    result = linregress(x, y)
    slope = result.slope
    intercept = result.intercept

    x_pred = np.arange(1880, 2051, 1)
    y_pred = slope * x_pred + intercept

    plt.plot(x_pred,y_pred, color='blue', label='The first line of best fit')

    # Create second line of best fit
    new_x = df.loc[df["Year"] >= 2000, 'Year']
    new_y = df.loc[df["Year"] >= 2000, 'CSIRO Adjusted Sea Level']
    new_result = linregress(new_x, new_y)
    new_slope = new_result.slope
    new_intercept = new_result.intercept
    x_new_pred = np.arange(2000, 2051, 1)
    y_new_pred = new_slope * x_new_pred + new_intercept

    plt.plot(x_new_pred,y_new_pred, color='red', label='The second line of best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
