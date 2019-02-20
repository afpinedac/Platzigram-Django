import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats.stats import pearsonr
import pandas as pd
import random
import math

df = pd.read_csv('article_A11_points.csv', sep=',')
file_data = [tuple(x) for x in df.values]

clusters = {
    'nflp': {
        'symbol': 'd',
        'color': 'red',
        'data': [],
        'description': 'No Feedback - Low Performance'
    },
    'nfmp': {
        'symbol': '>',
        'color': 'green',
        'data': [],
        'description': 'No Feedback - Medium Performance'
    },
    'nfhp': {
        'symbol': '<',
        'color': 'blue',
        'data': [],
        'description': 'No Feedback - High Performance'
    },
    'yflp': {
        'symbol': 'o',
        'color': 'brown',
        'data': [],
        'description': 'Yes Feedback - Low Performance'
    },
    'yfmp': {
        'symbol': 'v',
        'color': 'orange',
        'data': [],
        'description': 'Yes Feedback - Medium Performance'
    },
    'yfhp': {
        'symbol': '^',
        'color': 'purple',
        'data': [],
        'description': 'Yes Feedback - High Performance'
    }
}

for i in file_data:

    if i[1] <= 3:
        if i[0] <= 35000:
            clusters['nflp']['data'].append(i)
        elif i[0] <= 60000:
            clusters['nfmp']['data'].append(i)
        else:
            clusters['nfhp']['data'].append(i)
    else:
        if i[0] <= 35000:
            clusters['yflp']['data'].append(i)
        elif i[0] <= 60000:
            clusters['yfmp']['data'].append(i)
        else:
            clusters['yfhp']['data'].append(i)

for cluster, cluster_data in clusters.items():
    xs = [i[1] for i in cluster_data['data']]
    ys = [i[0] for i in cluster_data['data']]

    print(cluster_data)

    plt.plot(xs, ys, cluster_data['symbol'], color=cluster_data['color'], label="{}".format(cluster_data['description']))

plt.axis([0, 5.5, 0, 120000])
plt.xlabel('Given response')
plt.ylabel('Points')
plt.grid(True)
plt.legend(numpoints=1)
plt.show()
