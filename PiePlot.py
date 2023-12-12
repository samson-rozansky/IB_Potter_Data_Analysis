import csv
import scipy
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
import numpy as np
with open('bruh1.csv', 'r') as f:
    reader = csv.reader(f)
    stuff= []
    #start is 64 for median
    #start is 58 for single
    for row in reader:
        try:
            if(len(row[3])<1):
                continue
            int(row[0])
            #12
            for i in range(4,12):
                try:
                    stuff.append(row[60+i])
                except:
                    pass
        except:
            pass
    print(max(stuff),min(stuff))
    #between = 12.75
    # Create some data
