# Title: US_thanksgiving.py
# Desc: Python Intermediate Data Analysis with Pandas project from Dataquest, 
#       helping to practice Series and Dataframe objects.
# Date: 3/8/2017
# Note: thanksgiving.csv contains a survey information on American Thanksgiving
#       celebration. 
#       The dataset came from FiveThirtyEight.

import pandas
data = pandas.read_csv("thanksgiving.csv", encoding="Latin-1")

# Displays all column names
# data.columns

# Check how many people said "Yes" when asked if they celebrate Thanksgiving
# Keep only rows on which people said "Yes"
data["Do you celebrate Thanksgiving?"].value_counts()
data = data[data["Do you celebrate Thanksgiving?"] == "Yes"]

# Explore main dishes
data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()

tofurkey = data[data["""What is typically the main dish at your Thanksgiving 
                     dinner?"""] == "Tofurkey"]
tofurkey["Do you typically have gravy?"]

# How many people eat at least one pie?
apple_isnull = data["""Which type of pie is typically served at your 
                    Thanksgiving dinner? Please select all that apply. 
                    - Apple"""].isnull()
pumpkin_isnull = data["""Which type of pie is typically served at your 
                      Thanksgiving dinner? Please select all that apply. 
                      - Pumpkin"""].isnull()
pecan_isnull = data["""Which type of pie is typically served at your 
                    Thanksgiving dinner? Please select all that apply. 
                    - Pecan"""].isnull()
ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
ate_pies.value_counts()

# Findings:
#
# More people ate at least a pie than turkey

# Convert string of age group into an integer
# We are taking the first number of each group (i.e. 18 for 18 - 29)
def age_str_to_int (string):
    if pandas.isnull(string):
        return None
    number = string.split(" ")[0]
    number = number.replace("+", "")
    number = int(number)
    return number

data["int_age"] = data["Age"].apply(age_str_to_int)
data["int_age"].describe()

# Findings:
# 
# We are taking the first number of each group, so the numbers are probably 
# skewed to the left. When I look at the percentiles, the age distribution looks
# pretty evenly spread out.

# Convert string of income group into an integer
# We are taking the first number of each group (i.e. 18 for 18 - 29)
def inc_str_to_int (string):
    if pandas.isnull(string):
        return None
    number = string.split(" ")[0]
    if number == "Prefer":
        return None
    number = number.replace("$", "")
    number = number.replace(",", "")
    number = int(number)
    return number

data["int_income"] = data["""How much total combined money did all members of 
                          your HOUSEHOLD earn last year?"""].apply(inc_str_to_int)
data["int_income"].describe()


# Findings:
# 
# Since we are using the first number of each categories again, the numbers are 
# probably skewed to the left. The maximum number is 200,000, so that could skew
# the results as well. Mean seems high. Standard deviation is big.

# Are income and traveling correlated?
under_150000 = data[data["int_income"] < 150000]
under_150000["How far will you travel for Thanksgiving?"].value_counts()

over_150000 = data[data["int_income"] > 150000]
over_150000["How far will you travel for Thanksgiving?"].value_counts()

# Findings:
# 
# About 41 percent (281/689) of people who earn less than $150,000 will 
# celebrate Thanksgiving at their houses.
#
# About 48 percent (49/102) of people who earn more than $150,000 will celebrate 
# Thanksgiving at their houses. 
#
# There is some difference but not that much. $150,000 mark might be too high to 
# include the young people with less income that we wanted to test for.

# Are celebrating Thanksgiving with friends and age correlated?
data.pivot_table(index="""Have you ever tried to meet up with hometown friends 
                 on Thanksgiving night?""", 
                 columns='Have you ever attended a "Friendsgiving?"', 
                 values="int_age")

# Findings:
# 
# Attending a "Friendsgiving" lowers the mean age. 
# 
# There is not a big difference between the group that has only met up with 
# hometown friends on Thanksgiving night and the group that has done neither.
# 
# There is about 3 years difference, though, between the group that has only 
# attended a "Friendsgiving" and the group that has done both.



