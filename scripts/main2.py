import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats.stats import pearsonr
import pandas as pd
import random
import math
import sys
import numpy
from statistics import mean, median, stdev
from scipy import stats

# plt.figure(figsize=(3, 4))


df = pd.read_csv('C:\\xampp2\\htdocs\\ticademia2\\storage\\app\\research\\article_A1_math.csv', sep=',', header=None)
file_data = [tuple(x) for x in df.values]

"""
    [0] user_id
    [1] user_document
    [2] survey_q1   // las retroalimentaciones fueron acertadas
    [3] survey_q2   // seguias o nó la retroalimentación
    [4] unal_score
    [5] ticademia_tries_ratio
"""

data_survey_q1 = [i[2] for i in file_data]
data_survey_q2 = [i[3] for i in file_data]
data_unal_score = [float(i[4]) for i in file_data]
data_ticademia_tries_ratio = [i[5] for i in file_data]

# DIAGRAM ==== Perceived usefulness / Tries ratio
# plt.scatter(data_survey_q1, data_ticademia_tries_ratio, s=
print("============================================")
print("============================================")
print("============================================")
diagram_title = 'Perceived usefulness / Tries ratio'
print("Generating {}".format(diagram_title))
plt.xticks(range(1, 6))
plt.title(diagram_title)
plt.xlabel('Perceived usefulness')
plt.ylabel('Tries ratio')
ax = plt.axes()
ax.yaxis.grid(True)
groups = []
for i in range(1, 6):
    groups.append([k for idx, k in enumerate(data_ticademia_tries_ratio) if data_survey_q1[idx] == i])
plt.boxplot(groups)
plt.show()

for i, data in enumerate(groups):
    print("Group {} = {}".format(i + 1, stats.describe(data)))

# DIAGRAM ==== Perceived usefulness / Course score
# plt.scatter(data_survey_q1, data_unal_score, s=2)
print("============================================")
print("============================================")
print("============================================")

diagram_title = 'Perceived usefulness / Course score'
print("Generating {}".format(diagram_title))
plt.xticks(range(1, 6))
plt.yticks(np.arange(0, 5.5, 0.5))
plt.title(diagram_title)
plt.xlabel('Perceived usefulness')
plt.ylabel('Course score')
ax = plt.axes()
ax.yaxis.grid(True)

groups = []
for i in range(1, 6):
    groups.append([k for idx, k in enumerate(data_unal_score) if data_survey_q1[idx] == i])
plt.boxplot(groups)
plt.show()

for i, data in enumerate(groups):
    print("Group {} = {}".format(i + 1, stats.describe(data)))

# DIAGRAM ==== Feedback followed / Course score
# plt.scatter(data_survey_q2, data_unal_score, s=2)
diagram_title = 'Feedback followed / Course score'

print("============================================")
print("============================================")
print("============================================")
print("Generating {}".format(diagram_title))

plt.title(diagram_title)
plt.xlabel('Feedback followed')
plt.ylabel('Course score')
plt.xticks(range(1, 6))
plt.yticks(np.arange(0, 5.5, 0.5))
ax = plt.axes()
ax.yaxis.grid(True)

groups = []
for i in range(1, 6):
    groups.append([k for idx, k in enumerate(data_unal_score) if data_survey_q2[idx] == i])
plt.boxplot(groups)
plt.show()

for i, data in enumerate(groups):
    print("Group {} = {}".format(i + 1, stats.describe(data)))

print("===================")
print("===================")

# plt.plot(xs, ys, cluster_data['symbol'], color=cluster_data['color'], label="{}".format(cluster_data['description']))

clusters = {
    'nflp': {
        'symbol': 'd',
        'color': 'red',
        'data': [],
        'description': 'Low feedback acceptance - Low score',
        'avg': 0
    },
    'nfmp': {
        'symbol': '>',
        'color': 'green',
        'data': [],
        'description': 'Low feedback acceptance - Medium score',
        'avg': 0
    },
    'nfhp': {
        'symbol': '<',
        'color': 'blue',
        'data': [],
        'description': 'Low feedback acceptance - High score',
        'avg': 0
    },
    'mflp': {
        'symbol': 'p',
        'color': 'yellow',
        'data': [],
        'description': 'Medium feedback acceptance - Low score',
        'avg': 0
    },
    'mfmp': {
        'symbol': 'P',
        'color': 'cyan',
        'data': [],
        'description': 'Medium feedback acceptance - Medium score',
        'avg': 0
    },
    'mfhp': {
        'symbol': 'h',
        'color': 'gray',
        'data': [],
        'description': 'Medium feedback acceptance - High score',
        'avg': 0
    },
    'yflp': {
        'symbol': 'o',
        'color': 'brown',
        'data': [],
        'description': 'High feedback acceptance - Low score',
        'avg': 0
    },
    'yfmp': {
        'symbol': 'v',
        'color': 'orange',
        'data': [],
        'description': 'High feedback acceptance - Medium score',
        'avg': 0
    },
    'yfhp': {
        'symbol': '^',
        'color': 'purple',
        'data': [],
        'description': 'High feedback acceptance - High score',
        'avg': 0
    }
}

pu_tr = zip(data_survey_q2, data_unal_score)

lows = []
highs = []

for i in pu_tr:

    if i[0] < 3:
        if i[1] <= 2:
            clusters['nflp']['data'].append(i)
        elif i[1] <= 4:
            clusters['nfmp']['data'].append(i)
        else:
            clusters['nfhp']['data'].append(i)

        lows.append(i[1])

    elif i[0] == 3:
        if i[1] <= 2:
            clusters['mflp']['data'].append(i)
        elif i[1] <= 4:
            clusters['mfmp']['data'].append(i)
        else:
            clusters['mfhp']['data'].append(i)
    else:
        if i[1] <= 2:
            clusters['yflp']['data'].append(i)
        elif i[1] <= 4:
            clusters['yfmp']['data'].append(i)
        else:
            clusters['yfhp']['data'].append(i)

        highs.append(i[1])

for cluster, cluster_data in clusters.items():
    xs = [i[0] for i in cluster_data['data'] if i[0] > 0]
    ys = [i[1] for i in cluster_data['data'] if i[0] > 0]
    course_scores = [i[1] for i in cluster_data['data'] if i[0] > 0]
    clusters[cluster]['avg'] = pd.Series(course_scores).mean()
    clusters[cluster]['std'] = pd.Series(course_scores).std()
    clusters[cluster]['stats'] = stats.describe(course_scores)
    plt.plot(xs, ys, cluster_data['symbol'], color=cluster_data['color'], label="{}".format(cluster_data['description']))

plt.axis([0, 5.5, 0, 11])
plt.xlabel('Feeback followed')
plt.ylabel('Course score')
plt.grid(True)
plt.legend(numpoints=1)
plt.title('Feedback followed / Course score')
plt.figure(figsize=(10, 8))
plt.show()

for cluster, cluster_data in clusters.items():
    print("cluster={} <<>> avg={} <<>> n={}".format(cluster_data['description'], str(clusters[cluster]['avg']), len(clusters[cluster]['data'])))
    print("{}".format(str(clusters[cluster]['stats'])))

# print notes in cluster



