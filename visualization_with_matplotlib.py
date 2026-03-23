import matplotlib.pyplot as plt
import numpy as np
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
