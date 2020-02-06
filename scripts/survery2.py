from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

x = np.array([list(range(1, 8)) for i in range(1, 11)])
y = np.array([[min(2938, 300 * i) for j in range(1, 8)] for i in range(1, 11)])

xTicks = [i for i in range(1, 7)]
yTicks = [i for i in range(0, 3000, 300)]
xLim = [1, 7]
yLim = [0, 3000]
zLim = [0, 100]


# max: 82 - 2700
def plotNeuronalNetworks():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim(xLim)
    ax.set_ylim(yLim)
    ax.set_zlim(zLim)

    z = np.array([
        [53, 58, 61, 67, 65, 86, 91],
        [55, 64, 72, 80, 81, 85, 90],
        [56, 59, 67, 78, 82, 82, 87],
        [54, 62, 66, 72, 80, 81, 88],
        [54, 65, 72, 79, 82, 83, 89],
        [56, 60, 69, 78, 81, 85, 90],
        [55, 61, 65, 69, 82, 85, 87],
        [51, 65, 67, 79, 78, 82, 88],
        [50, 67, 72, 75, 81, 82, 90],
        [59, 66, 76, 79, 82, 85, 89]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks(xTicks)
    plt.yticks(yTicks)

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Neuronal Networks')
    plt.show()


# max: 82 - 2400
def plotNaiveBayes():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim(xLim)
    ax.set_ylim(yLim)
    ax.set_zlim(zLim)

    z = np.array([
        [61, 58, 61, 67, 75, 82, 92],
        [59, 64, 75, 80, 86, 91, 89],
        [56, 62, 70, 79, 85, 86, 86],
        [54, 66, 71, 76, 79, 85, 93],
        [56, 68, 75, 79, 81, 86, 90],
        [58, 63, 70, 75, 85, 87, 89],
        [60, 61, 66, 68, 75, 79, 82],
        [56, 67, 72, 78, 82, 85, 87],
        [58, 58, 71, 74, 82, 85, 88],
        [61, 66, 69, 82, 83, 84, 89]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks(xTicks)
    plt.yticks(yTicks)

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Naïve Bayes')
    plt.show()


# max: 86 - 2700
def plotAdaptativeBoosting():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim(xLim)
    ax.set_ylim(yLim)
    ax.set_zlim(zLim)

    z = np.array([
        [61, 63, 69, 75, 79, 85, 89],
        [58, 64, 75, 78, 85, 87, 89],
        [62, 62, 72, 76, 80, 85, 92],
        [55, 63, 77, 84, 86, 86, 90],
        [60, 67, 77, 79, 85, 87, 91],
        [54, 64, 70, 81, 85, 89, 89],
        [56, 60, 66, 71, 77, 85, 87],
        [59, 67, 72, 77, 82, 87, 88],
        [61, 70, 72, 76, 82, 86, 90],
        [57, 66, 65, 79, 86, 85, 91]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks(xTicks)
    plt.yticks(yTicks)

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Adaptative Boosting')
    plt.show()


# max: 80 - 2900
def plotRandomForest():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim(xLim)
    ax.set_ylim(yLim)
    ax.set_zlim(zLim)

    z = np.array([
        [54, 57, 65, 72, 82, 81, 87],
        [53, 59, 68, 72, 80, 85, 91],
        [57, 57, 56, 72, 71, 78, 90],
        [58, 61, 75, 73, 82, 78, 89],
        [59, 61, 72, 73, 79, 81, 88],
        [61, 67, 70, 75, 76, 85, 87],
        [60, 69, 72, 80, 81, 82, 86],
        [66, 70, 80, 82, 84, 86, 89],
        [67, 75, 72, 70, 79, 87, 92],
        [60, 62, 67, 70, 80, 85, 93]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks(xTicks)
    plt.yticks(yTicks)

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Random Forest')
    plt.show()


# max: 84 - 2700
def plotDecisionTree():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim(xLim)
    ax.set_ylim(yLim)
    ax.set_zlim(zLim)

    z = np.array([
        [53, 59, 65, 77, 82, 80, 90],
        [55, 55, 68, 66, 79, 78, 89],
        [56, 60, 64, 75, 72, 81, 87],
        [57, 65, 63, 70, 69, 75, 86],
        [62, 70, 72, 75, 78, 76, 90],
        [68, 71, 76, 82, 81, 84, 91],
        [62, 68, 75, 72, 85, 82, 87],
        [61, 75, 77, 82, 80, 85, 94],
        [59, 65, 72, 75, 85, 80, 91],
        [58, 79, 76, 75, 79, 85, 91]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks(xTicks)
    plt.yticks(yTicks)

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Decision Tree')
    plt.show()


plotNeuronalNetworks()
plotNaiveBayes()
plotAdaptativeBoosting()
plotRandomForest()
plotDecisionTree()
