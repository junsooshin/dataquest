# Title: recent_grad_unemployment.py
# Desc: The "Exploratory Data Visualization" guided project from Dataquest.
# Date: 3/10/2017
# Note: recent-grad.csv contains the survey information from American Community 
#       Survey on recent college graduates from 2010 to 2012.
#       The dataset came from FiveThirtyEight.

get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib
from pandas.tools.plotting import scatter_matrix
from pandas import Series

recent_grads = pd.read_csv("recent-grads.csv")
recent_grads.iloc[0]
recent_grads.head()
recent_grads.tail()
recent_grads.describe()

raw_data_count = len(recent_grads.index)
raw_data_count

recent_grads = recent_grads.dropna()
cleaned_data_count = len(recent_grads.index)
cleaned_data_count

recent_grads.plot(x="Sample_size", y="Median", kind="scatter", 
				  title="Median vs. Sample_size")
# The "Median vs. Sample_size" scatter plot does not show any clear correlation. 
# 
# Some findings are:
# - There are many points with under-800 sample size. 
# - The bottom-left of the chunk shows that there is perhaps a very-slight 
#   positive correlation. 
# - For the majors with less-than-1000 sample sizes, the medians vary widely 
#   from about \$20,000 to \$110,000. 
# - There are two possible outliers: a major with 4000+ sample size and \$40,000
#   median and a major with near 100 sample size and \$110,000 median.

recent_grads.plot(x="Sample_size", y="Unemployment_rate", kind="scatter", 
				  title="Umemployment_rate vs. Sample_size")
recent_grads.plot(x="Full_time", y="Median", kind="scatter",
	              title="Median vs. Full_time")
# The "Median vs. Full_time" scatter plot shows a similar pattern to the 
# "Median vs. Sample_size" scatter plot. It does not show any clear correlation.

recent_grads.plot(x="ShareWomen", y="Unemployment_rate", kind="scatter", 
				  title="Unemployment_rate vs. ShareWomen")
# The "Unemployment_rate vs. ShareWomen" scatter plot shows no correlation. It 
# is interesting to see that there are majors with near 0% or 100% share of 
# women.

recent_grads.plot(x="Men", y="Median", kind="scatter", title="Median vs. Men")
recent_grads.plot(x="Women",y="Median",kind="scatter", title="Median vs. Women")

recent_grads["Sample_size"].plot(kind="hist")
recent_grads["Sample_size"].hist(bins=25, range=(0,5000))
recent_grads["Median"].plot(kind="hist")
# The most common median salary range for college graduates is \$30,000 to 
# \$40,000.

recent_grads["ShareWomen"].plot(kind="hist")
# There are more classes with more women than men.

scatter_matrix(recent_grads[["Sample_size", "Median"]], figsize=(10,10))
scatter_matrix(recent_grads[["Sample_size", "Median", "Unemployment_rate"]], 
			   figsize=(10,10))
# Frankly, I do not think "Pandas, Scatter Matrix Plot" is useful in this case.

women_major = Series(recent_grads["ShareWomen"].values, 
					 index=recent_grads["Major"])
women_major.sort_values(ascending=False)

unrate_major = Series(recent_grads["Unemployment_rate"].values, 
	                  index=recent_grads["Major"])
unrate_major.sort_values(ascending=False)



