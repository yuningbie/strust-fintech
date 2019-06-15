#!/usr/bin/python3

import sys
import json
import numpy as np
import pandas as pd

data = pd.read_csv('data/eos.csv', delimiter = ',')
df = pd.DataFrame(data)
#print(df)

for col in data.columns: 
    print(col)



# find the columns for "date" and "price(USD)"





# calculate interday return (difference between price of 2 consecutive days)





# calculate volatility 30d (standard deviation of the interday return over the past 30 days)





# calculate the ROI 30d (difference between price of any day and price 30 days ago)




# sort the table based on volatility (small to big)




# select rows with volatility <=0.2
    #calculate correlation (linear regression: what is the slope?) of volatility and ROI


# select rows with volatility >0.2
    #calculate correlation (linear regression: what is the slope?) of volatility and ROI
