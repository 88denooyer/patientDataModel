import string
import config
import json
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from pprint import pprint
import csv
import names
import random


#with open(r'patient_data_set.csv', 'a', newline='') as csvfile:
#    fieldnames = ['timestamp', 'time_of_day',
#                  'patient_id',
#                  'patient_pain', 'patient_flex']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#   for i in range(1500):
#        patient_ident = i + 817435
#        date = '1/1/2019'
#        writer.writerow({'timestamp': date, 'time_of_day': '0900',
#                         'patient_id': patient_ident,
#                         'patient_pain': random.randint(1, 20), 'patient_flex': random.randint(1, 20)})\

# ========================
TAG = 'athletic'
PAIN_TOL = 'medium'
FILE_TAG = 'd1t1'
DAY = '1/1/2019'
TOD = '0900'
# ========================

with open(r'pds_' + TAG + '_' + PAIN_TOL + '_' + FILE_TAG + '.csv', 'a', newline='') as athfile:
    ath_fields = ['timestamp',
                  'tod',
                  'p_id',
                  'p_pain',
                  'p_flex',
                  'p_tag']
    writer = csv.DictWriter(athfile, fieldnames=ath_fields)
    for i in range(1500):
        p_ident = i + 817435
        day = DAY
        tod = TOD
        tag = TAG
        writer.writerow({'timestamp': day,
                         'tod': tod,
                         'p_id': p_ident,
                         'p_pain': random.randint(1, 9),
                         'p_flex': random.randint(1, 8),
                         'p_tag': tag})



"""
def get_data():
    if(os.path.exists('patient_data_set.csv')):
        print('--csv found')
        df = pd.read_csv('patient_data_set.csv', index_col=0)
    return df


df = get_data()
"""
#print('* df.head()', df.head(), sep="\n", end="\n\n")
#print('* df.tail()', df.tail(), sep="\n", end="\n\n")

