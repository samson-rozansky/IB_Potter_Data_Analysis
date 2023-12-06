import csv
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
import numpy as np
with open('bruh.csv', 'r') as f:
    reader = csv.reader(f)
    poverty = []
    graddy = []
    for row in reader:
        try:
            int(row[0])
            for i in range(4,12):
                try:
                    float(row[i])
                    float(row[8+i])
                    poverty.append(float(row[i]))
                    graddy.append(float(row[8+i]))
                except:
                    pass
        except:
            pass
    # Create some data
    xb = np.array(poverty)
    yb = np.array(graddy)
    # x = normalize([x])
    # y = normalize([y])
    
    sns.scatterplot(x=poverty, y=graddy)
    ax = sns.regplot(x=poverty, y=graddy,scatter_kws={"color": "black"}, line_kws={"color": "red"})
    # Plot the scatterplot
    # plt.scatter(x, y)
    ax.set_xlim([0,60])
    ax.set_ylim([50,100])
    
    plt.xlim(0, 60)
    plt.ylim(50, 100)
    plt.show()
    # # Show the plot
    # plt.show()
