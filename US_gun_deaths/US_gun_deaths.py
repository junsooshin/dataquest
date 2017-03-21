# Title: US_gun_deaths.py
# Desc: Python Intermediate project from Dataquest, helping to practice modules, 
#       enumeration, indexing, and scopes.
# Date: 3/1/2017
# Note: guns.csv contains information on gun deaths in the U.S. from 2012 to 
#       2014. 
#       The dataset came from FiveThirtyEight.

import csv
import datetime

file = open("guns.csv", "r")
data = list(csv.reader(file))

# get rid of the header row
headers = data[0]
data = data[1:]

years = [row[1] for row in data]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1

# explore data by months and years using the datetime objects
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) 
        for row in data]

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1

# explore data by sex and race
sex_counts = {}
race_counts = {}

for row in data:
    sex = row[5]
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1

for row in data:
    race = row[7]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

sex_counts
race_counts


# What I've learned so far:
# - A lot of male and a lot of white population have died by gun in the U.S. 
# from 2012 to 2014.
# 
# Questions:
# - Are these rates proportional to the general population? (i.e. are there this
# much more male and white population in the U.S?)
# - What are the reasons for this trend?


# read in the 2010 census data to find proportions by sex, race, etc.
file2 = open("census.csv", "r")
census = list(csv.reader(file2))

census

# keys are from gun.csv, and counts are from census.csv
mapping = {}
numbers = census[1]

mapping["Asian/Pacific Islander"] = int(numbers[14]) + int(numbers[15])
mapping["Black"] = int(numbers[12])
mapping["Hispanic"] = int(numbers[11])
mapping["Native American/Native Alaskan"] = int(numbers[13])
mapping["White"] = int(numbers[10])

race_per_hundredk = {}
for race, count in race_counts.items():
    race_per_hundredk[race] = count / mapping[race] * 100000

race_counts
mapping
race_per_hundredk
headers

# looking only at homicides
intents = [row[3] for row in data]
races = [row[7] for row in data]

homicide_race_counts = {}

for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts[race] += 1

homicide_race_per_hundredk = {}

for race, count in homicide_race_counts.items():
    homicide_race_per_hundredk[race] = count / mapping[race] * 100000

homicide_race_per_hundredk


# New findings:
# - Proportional to population, a lot of white and black Americans are involved 
# in gun deaths.
# - Proportional to population, Black Americans are most involved in homicide 
# gun deaths by far
# 
# Questions:
# - Where do these happen?
# - Why do these happen?

