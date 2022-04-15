import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Modified negative exponential function
def negex_function(x, a, b, k):
    return a * np.exp(b * x) + k

# Modified hugershoff function
def hugershoff_function(x, a, b, c, d):
    return a*(x**b)*np.exp(c*x) + d

# Attempt to fit a hugershoff curve to the series
def hugershoff(series):
    x = series.index.to_numpy()
    
    y = series.to_numpy()
    xi = np.arange(1, len(y)+1)
    pars, unk= curve_fit(hugershoff_function, xi, y, bounds=([0, -2, -np.inf, min(y)], [np.inf, 2, 0, max(y)]), 
                            p0=[max(y)-min(y), 0, 0, y[0]])
    a, b, c, d = pars

    yi = hugershoff_function(xi, a, b, c, d)

    plt.plot(x, y, "o", x, yi, "-")
    plt.show()
    return yi

# Attempt to fit a negative exponential curve to the series
def negex(series):
    x = series.index.to_numpy()
    
    y = series.to_numpy()
    xi = np.arange(1, len(y)+1)
    pars, unk= curve_fit(negex_function, xi, y, bounds=([0, -np.inf, 0], [np.inf, 0, np.inf]))
    a, b, k = pars

    yi = negex_function(xi, a, b, k)

    plt.plot(x, y, "o", x, yi, "-")
    plt.ylim(0, 1)
    plt.show()
    return yi

def gaussian(x, a, b, c):
    return a*np.exp(-np.power(x - b, 2)/(2*np.power(c, 2)))
    
# Equation of a straight line
def line_function(x, m, c):
    return (m * x) + c

# Fit a line to the series
def linear(series):
    x = series.index.to_numpy()
    y = series.to_numpy()
    pars, unk = curve_fit(line_function, x, y)
    m, c = pars
    yi = line_function(x, m, c)
    plt.plot(x, y, "o", x, yi, "-")
    plt.show()
    return yi