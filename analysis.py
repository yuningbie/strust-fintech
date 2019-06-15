#!/usr/bin/python3

import sys
import json
import glob
import numpy as np
import pandas as pd

# data = pd.read_csv('data/eos.csv', delimiter = ',')
# df = pd.DataFrame(data)
#print(df)

# for col in data.columns: 
    # print(col)

dataPath = "data/"
filenames = glob.glob(dataPath + "/*.csv")


def calculateMetrics(filename):
    print(filename)
    data = pd.read_csv(dataPath+filename+".csv", delimiter = ',')
    df = pd.DataFrame(data)
    
    # Calculate Interday Return:
    df_datePrice = pd.DataFrame(data, columns=['date', 'price(USD)'])
    df_InterdayRetrun = calculateInterdayReturn(df_datePrice)
    
    print(df_InterdayRetrun)
    return;

# find the columns for "date" and "price(USD)"
# for data in dataArr:
#     df = pd.DataFrame(data, columns=['date', 'price(USD)'])
#     columnNames = list(df.head(0))
    


# calculate interday return (difference between price of 2 consecutive days)
def calculateInterdayReturn(df):
    newColumn = df.set_index('date').diff()
    print(newColumn)
    df.loc[:, 'interday return'] = pd.Series(newColumn)
    return df


calculateMetrics("eos")


# calculate volatility 30d (standard deviation of the interday return over the past 30 days)





# calculate the ROI 30d (difference between price of any day and price 30 days ago)




# sort the table based on volatility (small to big)




# select rows with volatility <=0.2
    #calculate correlation (linear regression: what is the slope?) of volatility and ROI


# select rows with volatility >0.2
    #calculate correlation (linear regression: what is the slope?) of volatility and ROI
