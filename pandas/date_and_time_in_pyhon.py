import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
from pandas.tseries.offsets import BDay
from datetime import datetime
import pandas as pd
import numpy as np
from dateutil import parser
import os
os.system('clear')
### Native Python dates and times: datetime and dateutil ###

# Manually building a date using the datetime type:
date = datetime(year=2026, month=3, day=18)
print(date)
print()

# parsing dates from a variety of string formats using the dateutil module
print("The input to the parse method of parser from dateutil is - '18th of march 2026'")
date = parser.parse('18th of march 2026')
print(f"After parsing we have - {date}")
print(f"Year %Y - {date.strftime('%Y')}")
print(f"Month %m - {date.strftime('%m')}")
print(f"Day %d - {date.strftime('%d')}")
print(f"Day of Week - {date.strftime('%A')}")
print()

# strftime documentation - https://docs.python.org/3/library/datetime.html
# dateutil documentation - https://labix.org/python-dateutil

# The power of datetime and dateutil lies in their -
# flexibility and easy syntax.

# They break down -
# when you wish to work with large arrays of dates and times.

# just as lists of Python numerical variables are suboptimal
# compared to NumPy-style typed numerical arrays

# lists of Python datetime objects are suboptimal
# compared to typed arrays of encoded dates.

### Typed arrays of times: NumPy’s datetime64 ###
# The datetime64 dtype encodes dates as 64-bit integers,
# Thus allows arrays of dates to be represented very compactly.
date = np.array('2026-03-18', dtype=np.datetime64)
print(date, date.dtype)
print()

# Once we have this date formatted,
# we can quickly do vectorized operations on it.
print(date + np.arange(15))
# This line will create a list from current date to next 15 days.
# Output :- ['2026-03-18' '2026-03-19' '2026-03-20' '2026-03-21' '2026-03-22'
#            '2026-03-23' '2026-03-24' '2026-03-25' '2026-03-26' '2026-03-27'
#            '2026-03-28' '2026-03-29' '2026-03-30' '2026-03-31' '2026-04-01']
print()

### Dates and times in Pandas: Best of both worlds ###
# Pandas combines the ease of use of datetime and dateutil with
# The efficient storage and vectorized interface of numpy.datetime64.

# We can use Pandas tools to repeat the demonstration from above.
date = pd.to_datetime('18th march 2026')
print(date)  # Output - 2026-03-18 00:00:00
print()
print(date.strftime('%A'))  # Output - Wednesday
print()

# we can do NumPy-style vectorized operations directly on this same object.
print(date+pd.to_timedelta(np.arange(15), 'D'))
# This line will create a list from current date to next 15 days.
# Output -
# DatetimeIndex(['2026-03-18', '2026-03-19', '2026-03-20', '2026-03-21',
#                '2026-03-22', '2026-03-23', '2026-03-24', '2026-03-25',
#                '2026-03-26', '2026-03-27', '2026-03-28', '2026-03-29',
#                '2026-03-30', '2026-03-31', '2026-04-01'],
#                 dtype='datetime64[ns]', freq=None)
print()

### Pandas Time Series: Indexing by Time ###
# We can construct a Series object that has timeindexed data:
# Example -
index = pd.DatetimeIndex(
    ['2023-03-15', '2024-03-16', '2025-03-17', '2026-03-18'])
series1 = pd.Series([0, 1, 2, 3], index=index)
print(series1)
# Output -
# 2023-03-15    0
# 2024-03-16    1
# 2025-03-17    2
# 2026-03-18    3
# dtype: int64
print()

# Indexing Based on Dates:
print(series1['2025-03-15':'2026-03-18'])
# 2025-03-17    2
# 2026-03-18    3
# dtype: int64
print()

# Passing a year to obtain a slice of all data from that year:
print(series1['2026'])
# Output - 2026-03-18    3
# dtype: int64
print()

### Pandas Time Series Data Structures ###
# For time stamps, Pandas provides the Timestamp type.
# It is essentially a replacement for Python’s native datetime,
# but is based on the more efficient numpy.datetime64 data type.

# For time periods, Pandas provides the Period type.
# This encodes a fixedfrequency interval based on numpy.datetime64.

# For time deltas or durations, Pandas provides the Timedelta type.
# Timedelta is a more efficient replacement for -
# Python’s native datetime.timedelta type, and is based on numpy.timedelta64.

# The pd.to_datetime() function can parse a wide variety of formats.
# Passing a single date to pd.to_datetime() yields a Timestamp;
# Passing a series of dates by default yields a DatetimeIndex:

date = pd.to_datetime([datetime(2026, 3, 18),
                       '19th march 2026',
                       '2026-march-20',
                       '21-03-2026',
                       '20260322'
                       ])
print(date)
# Output -
# DatetimeIndex(['2026-03-18','2026-03-19','2026-03-20','2026-07-21',
#                '2026-03-22'], dtype='datetime64[ns]', freq=None)
print()

# To Convert DatetimeIndex to PeriodIndex,
# We can use to_period() function.
print(date.to_period('D'))
# Output -
# PeriodIndex(['2026-03-18', '2026-03-19', '2026-03-20', '2026-03-21',
#              '2026-03-22'], dtype='period[D]')
print()

# We can create a TimedeltaIndex by subtracting one date from another.
print(date-date[0])  # It is subtract the date at 0 index from every date.
# Output -
# TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'],
# dtype='timedelta64[ns]', freq=None)
print()

### Regular sequences ###
# Python’s range() and NumPy’s np.arange()
# turn a startpoint, endpoint, and optional stepsize into a sequence.
# Similarly, pd.date_range() accepts
# a start date, an end date, and an optional frequency code
# to create a regular sequence of dates.
# By default, the frequency is one day.

print(pd.date_range('2026-03-19', '2026-03-29'))
# Output - The Dates between these two dates will be printed.
# DatetimeIndex(['2026-03-19', '2026-03-20', '2026-03-21', '2026-03-22',
#                '2026-03-23', '2026-03-24', '2026-03-25', '2026-03-26',
#                '2026-03-27', '2026-03-28', '2026-03-29'],
#                 dtype='datetime64[ns]', freq='D')
print()

# The date range can be specified not with a start- and endpoint,
# but with a startpoint and a number of periods.
print(pd.date_range('2026-03-19', periods=10))
# Output - The 10 next dates are created from the starting date.
# DatetimeIndex(['2026-03-19', '2026-03-20', '2026-03-21', '2026-03-22',
#                '2026-03-23', '2026-03-24', '2026-03-25', '2026-03-26',
#                '2026-03-27', '2026-03-28'],
#                 dtype='datetime64[ns]', freq='D')
print()

# You can change the spacing by alternating the freq argument.
# By default it is D.
# We will construct a range of hourly timestamps.
print(pd.date_range('2026-03-19', periods=8, freq='h'))
# Output - DatetimeIndex(['2026-03-19 00:00:00', '2026-03-19 01:00:00',
#                         '2026-03-19 02:00:00', '2026-03-19 03:00:00',
#                         '2026-03-19 04:00:00', '2026-03-19 05:00:00',
#                         '2026-03-19 06:00:00', '2026-03-19 07:00:00'],
#                         dtype='datetime64[ns]', freq='h')
# The range is created based on hours.
print()

# To create regular sequences of period or time delta values,
# The very similar,
# pd.period_range() and pd.timedelta_range() functions are used.
print(pd.period_range('2026-03-19', periods=6, freq='M'))
# Period is created for the next 6 months.
# Output -
# PeriodIndex(['2026-03', '2026-04',
#              '2026-05', '2026-06',
#              '2026-07', '2026-08'],
#               dtype='period[M]')
print()

# For a sequence of durations increasing by an hour:
print(pd.timedelta_range(0, periods=10, freq='h'))
# Output -
# TimedeltaIndex(['0 days 00:00:00', '0 days 01:00:00', '0 days 02:00:00',
#                 '0 days 03:00:00', '0 days 04:00:00', '0 days 05:00:00',
#                 '0 days 06:00:00', '0 days 07:00:00', '0 days 08:00:00',
#                 '0 days 09:00:00'],
#                 dtype='timedelta64[ns]', freq='h')
print()

# Frequencies and Offsets -
# Listing of Pandas frequency codes
# Code      Description     Code    Description
#  D        Calendar day     B      Business day
#  W           Weekly
#  M         Month end       BM   Business month end
#  Q        Quarter end      BQ   Business quarter end
#  A          Year end       BA   Business year end
#  H           Hours         BH   Business hours
#  T          Minutes    - Depricated and 'min' should be used.
#  S          Seconds
#  L        Milliseonds
#  U        Microseconds
#  N        Nanoseconds

# Codes can be combined with numbers to specify other frequencies.
# For example, for a frequency of 2 hours 30 minutes,
# we can combine the hour (H) and minute (T) codes.
print(pd.timedelta_range(0, periods=10, freq='2h30min'))
# Output -
# TimedeltaIndex(['0 days 00:00:00', '0 days 02:30:00', '0 days 05:00:00',
#                 '0 days 07:30:00', '0 days 10:00:00', '0 days 12:30:00',
#                 '0 days 15:00:00', '0 days 17:30:00', '0 days 20:00:00',
#                 '0 days 22:30:00'],
#                 dtype='timedelta64[ns]', freq='150min')
print()

# All of these short codes refer -
# To specific instances of Pandas time series offsets,
# which can be found in the pd.tseries.offsets module.
# from pandas.tseries.offsets import BDay

# For example, we can create a business day offset directly.
print(pd.date_range('2026-03-19', periods=10, freq=BDay()))
# DatetimeIndex(['2026-03-19', '2026-03-20', '2026-03-23', '2026-03-24',
#                '2026-03-25', '2026-03-26', '2026-03-27', '2026-03-30',
#                '2026-03-31', '2026-04-01'],
#                 dtype='datetime64[ns]', freq='B')
print()

### Resampling, Shifting, and Windowing ###
# The ability to use dates and times as indices to
# intuitively organize and access data is an important
# piece of the Pandas time series tools.
# Pandas provides several additional time series–specific operations.

# pandas_datareader is kinda outdated for some sources
# yfinance is the industry standard workaround now
# import yfinance as yf
goog = yf.download('GOOG', start='2004-01-01', end='2016-01-01')

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()
sns.set()
ClosingData = goog['Close']
# plt.plot(ClosingData)
# plt.show()    - Commented to prevent the execution.

## Resampling and converting frequencies ##
# One common need for time series data is
# resampling at a higher or lower frequency.

# You can do this using the resample() method
# The much simpler asfreq() method.
# The primary difference between the two is that -
# resample() is fundamentally a data aggregation,
# while asfreq() is fundamentally a data selection.

## Time-shifts ##
# For computing time shift pandas provides: shift() and tshift().
# shift() shifts the data.
# while tshift() shifts the index.

## Rolling windows ##
# Rolling statistics are a third type,
# of time series–specific operation implemented by Pandas.

# These can be accomplished via,
# the rolling() attribute of Series and Data Frame objects,

# one-year centered rolling mean and standard deviation -
ClosingData = goog['Close'].squeeze()
rolling = ClosingData.rolling(365, center=True)
data = pd.DataFrame({
    'input': ClosingData,
    'one-year rolling mean': rolling.mean(),
    'one-year rolling std': rolling.std()
})
ax = data.plot(style=['-', '--', ':'])
ax.lines[0].set_alpha(0.3)
plt.show()
print()
