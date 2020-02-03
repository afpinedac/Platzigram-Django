import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats.stats import pearsonr
import pandas as pd
import random
import math

df = pd.read_csv('article_A11_kmeans.csv', sep=',')
file_data = [tuple(x) for x in df.values]

x = []
y = []
z = []

students = 0

with_extrapolation = False
for i in file_data:

    if i[1] == 0:
        continue

    students+=1

    if with_extrapolation:
        rand_fr = random.randint(1, 200)
        rand_ff = random.randint(max(0, rand_fr - random.randint(20, 50)), rand_fr);

        x.append(i[2] + rand_fr)  # feedback received
        y.append(i[3] + rand_ff)  # feedback followed
        z.append(i[1] + math.log1p(i[1]) + random.randint(5, 30))  # score
    else:
        x.append(i[2])  # feedback received
        y.append(i[3])  # feedback followed
        z.append(i[1])  # score

data = np.column_stack((x, y, z))

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# x = np.random.rand(10);
# y = np.random.rand(10);
# z = np.random.rand(10);

# ,

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("Feedback received")
ax.set_ylabel("Feedback Followed")
ax.set_zlabel("Scores")

#
ax.scatter(x, y, z, c=kmeans.labels_, cmap='rainbow')
plt.grid(False)
plt.legend(loc='best', bbox_to_anchor=(1, 1), prop={'size': 9})
plt.show()

corr = pd.DataFrame(data, columns=['received', 'followed', 'score'])

correlation = corr.corr(method='pearson')

print(correlation)
