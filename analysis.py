#!/usr/bin/python3

import sys
import json
import numpy as np
import pandas as pd

data = pd.read_csv('data/eos.csv', delimiter = ',')
df = pd.DataFrame(data)
print(df)