# Title: US_births.py
# Desc: Python programming: Beginner guided project on Dataquest
# Date: 2/22/2017
# Note: US_births_1994-2003_CDC_NCHS.csv was compiled by
#       FiveThirtyEight.

def read_csv(file_name):
    f = open(file_name, "r")
    string = f.read()
    string_list = string.split("\n")
    string_list = string_list[1:(len(string_list)-1)]
    final_list = []
    for date in string_list:
        int_fields = []
        string_fields = date.split(",")
        for field in string_fields:
            int_fields.append(int(field))
        final_list.append(int_fields)
    return(final_list)

def month_births(list_lists):
    births_per_month = {}
    for int_fields in list_lists:
        month = int_fields[1]
        births = int_fields[4]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return(births_per_month)

def dow_births(list_lists):
    births_per_day = {}
    for int_fields in list_lists:
        day = int_fields[3]
        births = int_fields[4]
        if day in births_per_day:
            births_per_day[day] += births
        else:
            births_per_day[day] = births
    return(births_per_day)

# general function that calculates total births for each specified column
def calc_counts(data, column):
    birth_dict = {}
    for int_fields in data:
        target = int_fields[column]
        births = int_fields[4]
        if target in birth_dict:
            birth_dict[target] += births
        else:
            birth_dict[target] = births
    return(birth_dict)

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_month_births = month_births(cdc_list)
cdc_day_births = dow_births(cdc_list)

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)