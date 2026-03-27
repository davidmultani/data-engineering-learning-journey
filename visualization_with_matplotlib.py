from sklearn.datasets import fetch_olivetti_faces
import matplotlib.dates as mpl
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.system('clear')
x = np.linspace(0, 10, 100)
#   plt.plot(x, np.sin(x))
#   plt.plot(x, np.cos(x))
#   plt.show()
# plt.show() starts an event loop,
# looks for all currently active figure objects,
# and opens one or more interactive windows that display your -
# figure or figures.
# the plt.show() command should be used only once per Python session.

# any cell within the notebook that creates a plot will
# embed a PNG image of the resulting graphic.

### Saving Figures to File ###
# Matplotlib allows to save figures in a wide variety of formats.
# savefig() command is used to save figure.


### Two Interfaces for the Price of One ###
# Matplotlib have dual interfaces -
# -- a convenient MATLAB-style state-based interface.
# -- a more powerful object-oriented interface.

## MATLAB-style interface ##
# -- The MATLAB-style tools are contained in the pyplot interface.

# create the first of two panels and set current axis.
#   plt.figure() # create a plot figure
#   plt.subplot(2, 1, 1)  # (rows,columns,plane number)
#   plt.plot(x, np.sin(x))

# create the second panel and set current axis.
#   plt.subplot(2, 1, 2)
#   plt.plot(x, np.cos(x))
#   plt.show()

# this interface is stateful -
# -- it keeps track of the "current figure and axes"
# -- you can get a reference to these using -
# -- the plt.gcf() (get current figure)
# -- the plt.gca() (get current axis)


##  -- Object-oriented interface -- ##
# It is useful when you want more control over your figure.
# Rather than depending on some notion of an "active" figure and axes.
# In object-oriented interface,
# plotting functions are methods of explicit Figure and Axes objects.

# Example -

# First create a grid of plots.
# ax will be an array of two Axes objects
#   fig, ax = plt.subplots(2)

# Call plot() method on the appropriate object.
#   ax[0].plot(x, np.sin(x))
#   ax[1].plot(x, np.cos(x))
#   plt.show()

# For complicated plots,
# the object oriented approach can become a necessity.
# We will switch between the MATLAB-style and object-oriented interfaces,
# depending on what is most convenient.

# In most cases,
# The difference is as small as switching plt.plot() and ax.plot().

### -- Simple line plots -- ###
# The simplest of all plots is -
# -- the visualization of a single function y=f(x).

# For all matplotlib, we start by creating a figure and an axes.
# The figure and axes can be created as follows -
# fig = plt.figure() # To create a figure.
# ax = plt.axes()    # To create a axes.

# The figure can be thought of as a single container that contains -
# all the objects representing axes, graphics, text and labels.

# The axes is what we see, a bounding box with ticks and labels,
# which will eventually contain the plot elements that make our visualization.

# We commonly use fig for figure instance and ax to refer to an axes instance.

# Once we have created an axes, we can use the ax.plot function to plot some data.

# For example -
#   fig = plt.figure()    ## Creating a figure
#   ax = plt.axes()       ## Creating a axes
#   ax.plot(x, np.sin(x)) ## Ploting the data
#   plt.show()

# Alternatively,
# We can use pylab interface.
# The pylab interface will create the figure and axes for us in the background.

# Example -
#   plt.plot(x, np.sin(x))
#   plt.plot(x, np.cos(x))
#   plt.show()

### -- Adjusting the Plot: Line Colors and Styles -- ###
# To control the color of the line and styles.
# - The plt.plot() function takes additional arguments that can ce used to specify these.

# - To adjust the color, you can use color keyword, which accepts a string argument for color.
# Example -
#       plt.plot(np.sin(x-0), color='blue')  # specify the color by name
#       plt.plot(np.sin(x-1), color='g')    # short color code (rgbcmyk)
#       plt.plot(np.sin(x-2), color='0.75')  # Grayscale between 0 and 1
#       plt.plot(np.sin(x-3), color='#FF0000')  # Hex code (rrggbb from 00 to FF)
#       plt.plot(np.sin(x-4), color=(1.0, 0.2, 0.3))  # RGB tuple, values 0 and 1
#       plt.plot(np.sin(x-5), color='chartreuse')  # all HTML color names supported
#       plt.show()
# If no color is specified,
# Matplotlib will automatically cycle through a set of default colors for multiple lines.


# To adjust the line style, we can use linestyle keyword -
# The various style are solid, dashed, dashdot, dotted.
# For short, you can use the -,--,-.,:
#   plt.plot(x, np.sin(x), linestyle='solid')    # or plt.plot(x, np.sin(x), linestyle='-')
#   plt.plot(x, np.cos(x), linestyle='dashed')   # plt.plot(x, np.sin(x), linestyle='--')
#   plt.plot(x, np.tan(x), linestyle='dashdot')  # plt.plot(x, np.sin(x), linestyle='-.')
#   plt.plot(x, np.sin(x-1), linestyle='dotted') # plt.plot(x, np.sin(x), linestyle=':')
#   plt.show()

# You can combine colorcode and style together -
# Example -
#   plt.plot(x, np.sin(x), '-g')    # solid green
#   plt.plot(x, np.cos(x), '--c')   # dashed cyan
#   plt.plot(x, np.tan(x), '-.k')   # dashdot black
#   plt.plot(x, np.sin(x-1), ':r')    # dotted red
#   plt.show()

# These single-character color codes reflect the standard abbreviations -
# -- RGB (Red Green Blue)
# -- CMYK (Cyan,Magenta,Yellow,BlacK)

### -- Adjusting the Plot: Axes Limits -- ###
# Matplotlib does the decent job of choosing default axes for your plot,
# But sometime it is nice to have a finer control.

# The most basic way to adjust axis limits is to use the -
# -- plt.xlim() and plt.ylim() nethods
# Example -
#       plt.xlim(0, 10)         # limits the x axis.
#       plt.ylim(-1.5, 1.5)     # limits the y axis.
#       plt.plot(x, np.sin(x))  # Ploting the values.
#       plt.show()              # showing the plotted data.

# if you want to reverse the axis then pass the arguments in xlim() and ylim in reverse.
# Example -
#       plt.xlim(10, 0)
#       plt.ylim(1.5, -1.5)
#       plt.plot(x, np.sin(x))
#       plt.show()

# A useful related method is plt.axis()
# (Note here the potential confusion between axes with an e and axis with i).
# The plt.axis() method allows you to set the x and y limits with a single call.
# you can pass a list that specifies [xmin , xmax , ymin , ymax].

# Example -
#       plt.axis([0, 10, -1.5, 1.5])
#       plt.plot(x, np.sin(x))
#       plt.show()

# To Automatically tighten the bounds around the current plot, we use -
#       plt.plot(x, np.sin(x))
#       plt.axis('tight')
#       plt.show()

# To ensure equal aspect ratio, i.e - one unit x is equal to one unit of y.
#       plt.plot(x, np.sin(x))
#       plt.axis('equal')
#       plt.show()

### --  Labeling plot  -- ###
# Their are methods that can be used to quickly set titles and axis.
# Example -
#       plt.plot(x, np.sin(x))
#       plt.title('A Sine Wave')
#       plt.xlabel('x value')
#       plt.ylabel('sin(x)')
#       plt.show()

# When you want to display multiple lines within a single axis, it can be done with plt.legend().
# Example -
#       plt.plot(x, np.sin(x), ':g', label="sin(x)")
#       plt.plot(x, np.cos(x), '-r', label='cos(x)')
#       plt.legend()  # It is used to combine multiple lines within a same axis.
#       plt.show()

# Most plt function translate directly to ax methods
# -- Such as plt.plot() -> ax.plot() and plt.legend() -> ax.legend()

# But functions to modify limits, labels, titles are bit modified.
# -- plt.xlabel() -> ax.set_xlabel()
# -- plt.ylabel() -> ax.set_ylabel()
# -- plt.xlim()   -> ax.set_xlim()
# -- plt.ylim()   -> ax.set_ylim()
# -- plt.title()  -> ax.set_title()

# Rather than calling these functions individually, we can use plt.set() method to set all these properties.
# Example -
#       ax = plt.axes()
#       ax.plot(x, np.sin(x), ':g')
#       ax.set(xlim=(0, 10), ylim=(-1.5, 1.5), xlabel='x',
#             ylabel='sin(x)', title='plot of x and sin(x)')
#       plt.show()

## - Simple Scatter plot - ##
# Scatter plot is quite similar as compared to line plot.
# Instead of points being joined with line segment.
# In Scatter plot, the points are represented individually with dot, circle, or other shape.
# Example -
#       plt.plot(x, np.sin(x), 'o', color='Black') # The plt.plot, same function can produce scatter plot.
#       plt.show()

### -- Scatter plot with plt.scatter() -- ###
# A more powerful function for scatter plot is plt.scatter() which works similar to plt.plot().
#       plt.scatter(x, np.sin(x), marker='o')
#       plt.show()

# A primary difference between plt.plot() function and plt.scatter() function is -
# -- The plt.scatter() allows more control over the individual points(size, face color, edge, color, etc).
# -- We can use the alpha to control the transparency level in the plot.

# plt.plot() is more efficient than plt.scatter() for large datasets -
# Reason -
# In the plt.scatter(), each point has to be rendered again and again which adds overhead. while,
# for plt.plot(), the appearance of points is done only once for the entire dataset.


### -- Basic Errorbars -- ###
#       dy = 0.8

#       np.random.randn(100) generates 100 random values from a normal (Gaussian) distribution
#       y = np.sin(x) + dy * np.random.randn(100)
#       plt.errorbar(x, y, yerr=dy, fmt='.k')
#       plt.show()

### -- Density and Contour Plots -- ###
# To plot the three-dimensional data into two dimensions.
# There are three matplotlib functions -
# 1. plt.contour for contour plots
# 2. plt.contourf for filled contour plots
# 3. plt.imshow for showing images

#       def cordinates(x, y):
#         return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


# Example -
#       y = np.linspace(0, 10, 100)
#       X, Y = np.meshgrid(x, y)
#       Z = cordinates(X, Y)
#       plt.contour(X, Y, Z, cmap='RdGy') # cmap is used to color code the lines
#       plt.contourf(X, Y, Z, 20, cmap='RdGy') # contourf is used to blend the lines in the plot
#       plt.colorbar() # It creates a additional axis(bar) with the labeled color information.
#       plt.show()

## -- Example of histogram -- ##
#       data = np.random.randn(1000)
#       plt.hist(data)
#       plt.show()
# hist() function provides the options to tune both the calculations and the display -
#       plt.hist(data, bins=30, alpha=0.5,
#               histtype='stepfilled', color='steelblue', edgecolor=None)
#       plt.show()

# Example of creating multiple transparent histogram overlaping each other -
# We will store the options for plt.hist() function in the kwargs as dictionary for reusability.
#       x1 = np.random.normal(0, 0.8, 1000)
#       x2 = np.random.normal(-2, 1, 1000)
#       x3 = np.random.normal(3, 2, 1000)
#       kwargs = dict(histtype='stepfilled', alpha=0.3, bins=40)
#       plt.hist(x1, **kwargs)
#       plt.hist(x2, **kwargs)
#       plt.hist(x3, **kwargs)
#       plt.show()

# To count the number of points in a given histogram, we can use np.histogram -
# Example -
#       data = np.random.randn(1000)
#       counts, bin_edges = np.histogram(data, bins=5)
#       print(counts)

## -- plt.hist2d: Two-dimensional histogram -- ##
# Example -
#       mean = [0, 0]
#       cov = [[0, 1], [1, 2]]
#       x, y = np.random.multivariate_normal(mean, cov, 10000).T
#       plt.hist2d(x, y, bins=40, cmap='Blues')
#       plt.colorbar().set_label('counts in bin')
#       plt.show()

## -- plt.hexbin: Hexagonal binnings -- ##
# It represents a two-dimensional dataset binned within a grid of hexagons
#       mean = [0, 0]
#       cov = [[0, 1], [1, 2]]
#       x, y = np.random.multivariate_normal(mean, cov, 10000).T
#       plt.hexbin(x, y, bins=40, gridsize=40, cmap='Blues')
#       plt.colorbar().set_label('counts in bin')
#       plt.show()

### --- Customizing Plot Legends --- ###
# First we will create the simple legend using ax.legend() function.
#       ax = plt.subplot()
# Their is a difference between plt.subplot and plt.subplots.
# The subplot only return one argument while subplot returns the 2 arguments.
# Example of subplot - ax = plt.subplot() # returned one argument
# Example of subplots - fig, ax = plt.subplots() # returned two arguments.
#       ax.plot(x, np.sin(x), linestyle='-', label='sin(x)')
#       ax.plot(x, np.cos(x), linestyle='--', label='cos(x)')
#       ax.set_xlabel('x values')
#       ax.set_ylabel('sin(x) values')
#       ax.set_title('relationship between x and sin(x)')
#       ax.axis('equal')

# loc to specify the labels location and ncol for number of columns(sin(x) in one col and cos(x) in other)
# we can also place the labels inside the box using (fancybox=True) and can give shadow (shadow=True)
#       ax.legend(loc='lower center', ncol=2, fancybox=True,
#                 shadow=True, framealpha=1, borderpad=1)
#       plt.show()

### --- Customizing Colorbars --- ###
# a colorbar is a separate axes that can provide a key for the meaning of colors in a plot.
# A simple colorbar can be created with the plt.colorbar() function.
# We can specify the colormap using cmap argument to the plotting function that is creating the visualization.

## -- Choosing the colormap -- ##
# Their are mainly three categories of colormaps:

# 1. Sequential colormaps -
# -- These consists of one continuous sequence of colors. example - binary or viridis.

# 2. Divergent colormaps -
# -- These usually contains two distinct colors which show positive and negative deviations from a mean.
# -- (e.g - RdGy,BuRd)

# 3. Qualitative colormaps -
# -- These mix colors with no particular sequence. (e.g - rainbow or jet)

### --- Multiple Subplots --- ###
# subplots are groups of smaller axes that can exist together within a single figure.
# These subplots might be insets, grids of plots, or other more complicated layouts.

## -- plt.axes: Subplots by Hand -- ##
# By default this creates a standard axes object that fills the entire figure.

# plt.axes() takes optional arguments -
# It is a list of four numbers in the figure coordinate system.
# These numbers represent [bottom,left,width,height] in the figure coordinate system.
# It ranges from 0 at the bottom left of the figure to 1 at the top right of the figure.
# Exmple -
#   plt.axes() # Standard axes
#   plt.axes([0.65,0.65,0.2,0.2]) # It will create an inset axes at the top-right corner.
#   plt.show()

# Similarly, In Object-Oriented Interface we can use fig.add_axes()
# Example - We will create a two vertically stacked axes.
#       fig = plt.figure()
#       ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], ylim=(-1.2, 1.2)
#                          )  # creating the top axes
#       ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2)
#             #                  )  # creating the bottom axes
#       ax1.plot(x, np.sin(x)) # plotting the top axes
#       ax2.plot(x, np.cos(x)) # plotting the bottom axes
#       plt.show()

## -- plt.subplot: Simple Grids of Subplots -- ##
# If we want to align multiple subplot of rows and columns in one axes then -
# We can use the plt.subplot() function.
# The subplot takes 3 integer arguments -
# -- the number of rows, the number of columns and the index of the plot
#       for i in range(1, 7):
#           plt.subplot(2, 3, i)
#           plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')
# 0.5,0.5 is the location of the text in the subplot and str((2,3,i) is the text)
#       plt.show()

# To adjust the spacing between the plots - we can use plt.subplots_adjust() function.
# we will use hspace and wspace arguments of plt.subplots_adjust.
# By specifing the spacing along the height and width of the figure.
# Example -
#       fig = plt.figure()
#       fig.subplots_adjust(hspace=0.4, wspace=0.4)
#       for i in range(1, 7):
#           ax = fig.add_subplot(2, 3, i)
#           ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')
#       plt.show()

### --- plt.subplots: The Whole Grid in One Go --- ###
# The plt.subplots is easier to use
# Rather than creating a single subplot,
# this function creates a full grid of subplots in a single line and return numPy array.
# By specifying the sharex and sharey we have automatically removed inner labels of grid.
# Example -
#       fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
#       plt.show()

# Now we will label the subplots using standard array indexing notation -
# axes are in a two dimensional array, indexed by [row, col]
#       fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
#       for i in range(2):
#           for j in range(3):
#               ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha='center')
#       plt.show()

### --- plt.GridSpec() --- ###
# plt.GridSpec() function is the interface that is recognized by the plt.subplot()
# Example -
#       grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.4)
#       plt.subplot(grid[0, 0])
#       plt.subplot(grid[0, 1:])
#       plt.subplot(grid[1, :2])
#       plt.subplot(grid[1, 2])
#       plt.show()

# Example : Effect of Holidays on US Births #
#       births = pd.read_csv(
#           'https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv')
#       quartiles = np.percentile(births['births'], [25, 50, 75])
#       med, stddiv = quartiles[1], 0.75 * (quartiles[2] - quartiles[0])
#       births = births.query(
#           '(births > @med - 5 * @stddiv) and (births < @med + 5 * @stddiv)')
#       births = births.dropna(subset=['day'])
#       births['day'] = births['day'].astype(int)
#       births.index = pd.to_datetime(
#           ((10000 * births.year) + (100 * births.month) + births.day), format='%Y%m%d')
#       births_by_date = births.pivot_table(
#           'births', [births.index.month, births.index.day])
#       births_by_date.index = [datetime(2012, month, day)
#                               for (month, day) in births_by_date.index]
#       fig, ax = plt.subplots(figsize=(12, 4))
#       births_by_date.plot(ax=ax)
#       # Adding labels to the plot
#       style = dict(size=10, color='grey')
#       ax.text('2012-1-1', 3950, "New Year's Day", **
#             style)  # ('Date',Births_value,label)
#       ax.text('2012-7-4', 4250, "Independence Day", ha='center', **style)
#       ax.text('2012-9-4', 4850, "Labour Day", ha='center', **style)
#       ax.text('2012-10-31', 4600, "Halloween", ha='center', **style)
#       ax.text('2012-11-25', 4450, "Thanksgiving", ha='center', **style)
#       ax.text('2012-12-25', 3850, "Christmas", ha='right', **style)
#
#       # Labelling the Axes -
#       ax.set(title='USA births by day of year', ylabel='average daily births')
#
#       # Format the x axis with centered month labels -
#       # Import matplotlib.dates as mpl
#       ax.xaxis.set_major_locator(mpl.MonthLocator())
#       ax.xaxis.set_minor_locator(mpl.MonthLocator(bymonthday=15))
#       ax.xaxis.set_major_formatter(plt.NullFormatter())
#       ax.xaxis.set_minor_formatter(mpl.DateFormatter('%h'))
#       plt.show()

### --- Customizing Ticks --- ###
# In this section,
# We will learn to adjust the tick locations and formatting for the particular plot type.
# Each axes has attributes xaxis and yaxis, which in turn have attributes that contains -
# - all the properties of the lines, ticks, labels that makes up the axes.

## -- Hidding Ticks or Labels -- ##
# You can hide ticks or labels using plt.NullLocator() and plt.NullFormater().
# Example -
# ax.yaxis.set_major_locator(plt.NullLocator()) # Removed the ticks(labels as well)
# ax.xaxis.set_major_formatter(plt.NullFormater()) # Removed the labels but kept gridlines.

# Example -
#       faces = fetch_olivetti_faces().images
#
#       fig, ax = plt.subplots(5, 5, figsize=(5, 5))
#       fig.subplots_adjust(hspace=0, wspace=0)
#
#       for i in range(5):
#           for j in range(5):
#               ax[i, j].xaxis.set_major_locator(plt.NullLocator())
#               ax[i, j].yaxis.set_major_locator(plt.NullLocator())
#               ax[i, j].imshow(faces[10 * i + j], cmap='bone')
#       plt.show()

## -- Reducing or Increasing the number of Ticks -- ##
# Example -
#       fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
#       plt.show()
# To specify the maximum number of ticks , We can use plt.MaxNLocator()
# Example -
fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
plt.show()
