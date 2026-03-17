import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
sns.set()
os.system('clear')
# GroupBy: Split, Apply, Combine
# The split step involves breaking up and grouping a DataFrame depending on the value of the specified key.
# The apply step involves computing some function, usually an aggregate, transformation, or filtering, within the individual groups.
# The combine step merges the results of these operations into an output array.

# We can compute the most basic split-apply-combine operation with the groupby() method of DataFrames, passing the name of the desired key column:
# df.groupby('key')

df = pd.DataFrame({"key": ['a', 'b', 'c', 'a', 'b', 'c'],
                   "data1": np.random.randint(0, 10, 6),
                   "data2": np.random.randint(0, 10, 6)},
                  columns=['key', 'data1', 'data2'])

# the aggregate() method allows for even more flexibility. It can take a string, a function, or a list thereof, and compute all the aggregates at once.
print(df.groupby('key').aggregate(['min', 'median', 'max']))
print()

# Another useful pattern is to pass a dictionary mapping column names to operations to be applied on that column:
print(df.groupby('key').aggregate({
    "data1": "min",
    "data2": "max"
}))
print()

## Filtering ##

# A filtering operation allows you to drop data based on the group properties.
print(df)
print()

# For example, we might want to keep all groups in which the standard deviation is larger than some critical value:


def filter_func(x):
    return (x['data2']).std() > 1


# The filter() function should return a Boolean value specifying whether the group passes the filtering.
print(df.groupby('key').filter(filter_func))
print()

## Transformation ##
# transformation can return transformed version of the full data to recombine.
# A common example is to center the data by subtracting the group-wise mean:
print(df.groupby('key').transform(lambda x: x-x.mean()))
print()


# Apply() Method:
# The apply() method lets you apply an arbitrary function to the group results.
# The function should take a DataFrame, and return either a Pandas object (e.g., DataFrame, Series) or a scalar.

def apply_function(x):
    # x is the DataFrame of group Values
    x['data1'] *= x['data2']
    return x


# apply() method is deprecated
print(df.groupby('key').apply(apply_function, include_groups=False))
print(df.groupby('key').aggregate(["sum"]))
print(df.groupby(df['key']).sum())
print()

# A dictionary or series mapping index to group
df = df.set_index('key')
mapping = {"a": "vowel", "b": "consonant", "c": "consonant"}
print(df.groupby(mapping).sum())
print()

# Example on Demo Dataset of planets
planet = sns.load_dataset('planets')
# converting year like 1989 to 198 and then multiply by 10 to get 1980
decades = 10*(planet['year']//10)
# Converted the year to string and going concat with 's'
decades = decades.astype(str) + "s"
decades.name = 'decade'  # Setting the name
grouped_data = planet.groupby(['method', decades])[  # grouping by method and year
    'number'].sum().unstack().fillna(0)
print(grouped_data)
print()


# Pivot Tables
# The pivot table takes simple columnwise data as input,
# and groups the entries into a two-dimensional table that
# provides a multidimensional summarization of the data.

# We will use demo dataset of titanic ship to find how many people survived
print()
print("Survival rate of passengers on the ship according to class")
titanic = sns.load_dataset('titanic')
print(titanic.head())
survival_rate = titanic.groupby(['sex', 'class'], observed=False)[
    'survived'].aggregate('mean').unstack()
print(survival_rate)
# we are dealing with two dimensional table so the previous approach can be confusing
# So to remove confusion we will simplify the code.
# We Will use pivot table to acheive this same thing.

pivot_table = titanic.pivot_table(
    'survived', index='sex', columns='class', observed=False)
# This is much simpler and easy to read code.
print()
print("The pivot table is -")
print(pivot_table)
print()

## Multilevel Pivot Table ##
# we might be interested in looking at age as a third dimension.
# We’ll bin the age using the pd.cut function.

age = pd.cut(titanic['age'], [0, 18, 80])
age_wise_pivot_table = titanic.pivot_table(
    'survived', index=['sex', age], columns='class', observed=False)
print(age_wise_pivot_table)
print()

fare = pd.cut(titanic['fare'], 2)
fare_wise_pivot_table = titanic.pivot_table(
    'survived', index=['sex', age], columns=[fare, 'class'], observed=False)
print(fare_wise_pivot_table)
# The result is a four-dimensional aggregation with hierarchical indices
print()

# The full call signature of the pivot_table method of DataFrames is as follows:
# call signature as of Pandas 0.18
# DataFrame.pivot_table(data, values=None, index=None, columns=None,
# aggfunc='mean', fill_value=None, margins=False,
# dropna=True, margins_name='All')

# Applied Aggregation function
print(titanic.pivot_table(index='sex', columns='class',
                          aggfunc={'survived': 'sum', 'fare': 'mean'}, observed=False))
print()

# it’s useful to compute totals along each grouping.
# This can be done via themargins keyword.
print(titanic.pivot_table(['survived'],
      index='sex', columns='class', margins=True, margins_name='total', observed=False))
print()

# Birthrate Data
births = pd.read_csv(
    "https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv")
print(births.head())
print()

# we will use the built-in plotting tools in Pandas to visualize the total number of births by year
births.pivot_table('births', index='year',
                   columns='gender', aggfunc='sum').plot()
plt.ylabel('total births per year')
# plt.show() # commented it out to prevent the execution.


# We start by cleaning the data a bit, removing outliers caused by mistyped dates
# (e.g., June 31st) or missing values (e.g., June 99th).
# One easy way to remove these all at once is to cut outliers;
# we’ll do this via a robust sigma-clipping operation
percentiles = np.percentile(births['births'], [25, 50, 75])

# Median of the births
med = percentiles[1]

# We have calculated the standard deviation
standard_deviation = 0.74 * (percentiles[2]-percentiles[0])

# We have selected only those records in which births greater than median - 5 * standard deviation
# and births less than median + 5 * standard deviation.
births = births.query(
    "(births > @med - 5 * @standard_deviation) & (births < @med + 5 * @standard_deviation)")

# Converting the births['day'] to int type
births['day'] = births['day'].astype(int)

# Finally, we can combine the day, month, and year to create a Date index.
births.index = pd.to_datetime(
    (10000*births['year']+100*births['month']+births['day']), format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek

# Adding the decade column in the births dataset
births['decade'] = 10 * (births['year']//10)

# Using this we can plot births by weekday for several decades
births.pivot_table('births', index='dayofweek',
                   columns='decade', aggfunc='mean').plot()

plt.xticks(range(7))
# This line sets the positions of the ticks on the x-axis.
# Range(7) generates numbers: 0, 1, 2, 3, 4, 5, 6
# So matplotlib creates 7 tick positions on the x-axis.
# 0   1   2   3   4   5   6
# |   |   |   |   |   |   |
# This is useful when your data represents 7 days of the week.

plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
# plt.gca() ==>> gca = Get Current Axes
# means: "Give me the current plot's axis so I can change its settings."
# set_xticklabels([...]) ==>> This function replaces the numeric tick labels with custom labels.
# Instead of:
#  0    1   2    3    4   5   6
# you will see:
# Mon Tues Wed Thurs Fri Sat Sun

# ylabel is used to set the label of y axis.
plt.ylabel('mean births by day')
print(births.head())
# plt.show() #Commented to Prevent the execution.


# Another interesting view is to plot the mean number of births by the day of the year.
# Let’s first group the data by month and day separately:
birth_by_day = births.pivot_table(
    'births', index=[births.index.month, births.index.day])

# let’s turn these months and days into a date by associating them with a dummy year variable.
birth_by_day.index = [pd.to_datetime((2012, month, day), format='%m%d')
                      for (month, day) in birth_by_day.index]
