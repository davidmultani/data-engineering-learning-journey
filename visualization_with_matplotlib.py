import matplotlib.pyplot as plt
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
plt.scatter(x, np.sin(x), marker='o')
plt.show()
