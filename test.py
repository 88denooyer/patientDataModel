import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

train = pd.read_csv('./__DATA_FOLDER/athletic_high_1-7-2019_0900.csv')
test = pd.read_csv('./__DATA_FOLDER/inactive_low_1-7-2019_0900.csv')
train['Type'] = 'Train'
test['Type'] = 'Test'
fullData = pd.concat([train, test], axis=0, sort=False)
fullData.columns
fullData.head(10)
fullData.describe()
print(fullData)