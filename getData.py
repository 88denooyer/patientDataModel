import string
import config
import json
import os

from pprint import pprint

with open('../randomDataGen/average.json') as data_file:
    data = json.load(data_file)

pain_list = []
flex_list = []


# simple function that will get sum of array items
def get_sum(array):
    sum_of_parts = 0
    for i in range(0, len(array)):
        sum_of_parts += array[i]
    pprint(sum_of_parts)


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
        pain_list.append(got_data[i]['pain_index'])


# does all mapping and appending to the global array defined in function
define_pain_path('GOOD_PATIENT', 'GPD1.json')
define_flex_path('GOOD_PATIENT', 'GPD1.json')
pprint('Pain Sum total')
# gets the sums
get_sum(pain_list)
pprint('Flex Sum total')
get_sum(flex_list)

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
