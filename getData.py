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

day1_pain = []
day2_pain = []
day3_pain = []
day4_pain = []
day5_pain = []
day6_pain = []
day7_pain = []


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


def get_array_day(day_num):
    day_list = {1: day1_pain,
                2: day2_pain,
                3: day3_pain,
                4: day4_pain,
                5: day5_pain,
                6: day6_pain,
                7: day7_pain}
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
def define_pain_path(path, name):
    with open('./DATA_SETS/' + path + '/' + name) as file_loc:
        got_data = json.load(file_loc)
    # prints entire file
    # pprint(got_data)
    # *returns* the first patient's flex index
    for i in range(0, 1000):
        # print(got_data[i]['pain_index'])
        # pain_list.append(got_data[i]['pain_index'])
        get_array_day(1).append(got_data[i]['pain_index'])


# does all mapping and appending to the global array defined in function
# define_pain_path('GOOD_PATIENT', 'GPD1.json')
# define_flex_path('GOOD_PATIENT', 'GPD1.json')
define_pain_path(path_list[0], good_name_list[0])
pprint(get_sum(pain_list))
pprint(get_array_day(1))

"""
get each daily pain data points for GOOD_DATA
store each daily data set in an array
x0 = d1, x1 = d2, ... xn = dn+1
y = all pain data points for xn
"""

"""
# gets the sums
pprint('Pain Sum total')
get_sum(pain_list)
pprint('Flex Sum total')
get_sum(flex_list)
"""

# pprint(pain_list)
# pprint('END')
# pprint(flex_list)


# all garbage testing for trying different things
"""
pprint(define_file_path('GOOD_PATIENT', 'GPD1.json'))
pprint(define_file_path('GOOD_PATIENT', 'GPD2.json'))
pprint(define_file_path('GOOD_PATIENT', 'GPD3.json'))
pprint(define_file_path('GOOD_PATIENT', 'GPD4.json'))
pprint(define_file_path('GOOD_PATIENT', 'GPD5.json'))
pprint(define_file_path('GOOD_PATIENT', 'GPD6.json'))
pprint(define_file_path('GOOD_PATIENT', 'GPD7.json'))
"""

"""
def readFile(filename):
    filehandle = open(filename)
    print(filehandle.read())
    filehandle.close


fileDir = os.path.dirname(os.path.relpath('__file__'))
filename = os.path.join(fileDir, '../randomDataGen/average.json')
readFile(filename)

readFile(filename)
"""
