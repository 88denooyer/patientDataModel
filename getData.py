import string
import config
import json
import os
import matplotlib.pyplot as plt

from pprint import pprint

with open('../randomDataGen/average.json') as data_file:
    data = json.load(data_file)

path_list = ['GOOD_PATIENT', 'AVERAGE_PATIENT', 'POOR_PATIENT']
good_name_list = ["GPD1.json", 'GPD2.json', 'GPD3.json', 'GPD4.json', 'GPD5.json', 'GPD6.json', 'GPD7.json']
avg_name_list = ['AVGD1.json', 'AVGD2.json', 'AVGD3.json', 'AVGD4.json', 'AVGD5.json', 'AVGD6.json', 'AVGD7.json']
poor_name_list = ['PPD1.json', 'PPD2.json', 'PPD3.json', 'PPD4.json', 'PPD5.json', 'PPD6.json', 'PPD7.json']
pain_list = []
flex_list = []
#########################################
day1_pain = []
day2_pain = []
day3_pain = []
day4_pain = []
day5_pain = []
day6_pain = []
day7_pain = []
#########################################
day1_flex = []
day2_flex = []
day3_flex = []
day4_flex = []
day5_flex = []
day6_flex = []
day7_flex = []
_day = 5


# simple function that will get sum of array items
def get_sum(array):
    sum_of_parts = 0
    for i in range(0, len(array)):
        sum_of_parts += array[i]
    return sum_of_parts


"""
this function below is used to return the individual day array
so when we call it later below,
it can be called as like get_array_day(2) which will return the
day2_pain array which makes it easier to call
later in the pain and flex path functions
"""


def get_flex_day(day_num):
    day_list = {1: day1_flex,
                2: day2_flex,
                3: day3_flex,
                4: day4_flex,
                5: day5_flex,
                6: day6_flex,
                7: day7_flex
    }
    if 7 < day_num < 0:
        raise Exception('Must be positive integer between 1 and 7')
    else:
        return day_list.get(day_num)


def get_pain_day(day_num):
    day_list = {1: day1_pain,
                2: day2_pain,
                3: day3_pain,
                4: day4_pain,
                5: day5_pain,
                6: day6_pain,
                7: day7_pain}
    if 7 < day_num < 0:
        raise Exception('Must be a positive integer between 1 and 7')
    else:
        return day_list.get(day_num)


# gets path for wanted file, finds the flex index part of the object
# appends i - 1 data to array
def define_flex_path(path, name):
    with open('./DATA_SETS/' + path + '/' + name) as file_loc:
        got_data = json.load(file_loc)
        for i in range(0, 1000):
            flex_list.append(got_data[i]['flex_index'])


# does the same as above except with pain
# see the comments for different testings
def define_pain_path(path, name, day):
    with open('./DATA_SETS/' + path + '/' + name) as file_loc:
        got_data = json.load(file_loc)
    # prints entire file
    # pprint(got_data)
    # *returns* the first patient's flex index
    for i in range(0, 1000):
        # print(got_data[i]['pain_index'])
        # pain_list.append(got_data[i]['pain_index'])
        get_pain_day(day).append(got_data[i]['pain_index'])


# does all mapping and appending to the global array defined in function
define_pain_path(path_list[0], good_name_list[0], _day)
# pprint(get_pain_day(_day))
pprint(get_sum(get_pain_day(_day)))


"""
get each daily pain data points for GOOD_DATA
store each daily data set in an array
x0 = d1, x1 = d2, ... xn = dn+1
y = all pain data points for xn
"""