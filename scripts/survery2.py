from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

x = np.array([list(range(1, 8)) for i in range(1, 11)])
y = np.array([[min(2938, 300*i) for j in range(1,8)] for i  in range(1, 11)])

# max: 82 - 2700
def plotNeuronalNetworks():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 7])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    z = np.array([
        [53, 45, 52, 53, 45, 52, 1],
        [55, 52, 44, 55, 52, 44, 1],
        [56, 55, 56, 56, 55, 56, 1],
        [57, 56, 57, 57, 56, 57, 1],
        [62, 61, 60, 62, 61, 60, 1],
        [68, 60, 69, 68, 60, 69, 1],
        [72, 68, 65, 72, 68, 65, 1],
        [75, 76, 59, 75, 76, 59, 1],
        [75, 82, 76, 75, 82, 76, 1],
        [75, 79, 76, 75, 79, 76, 1]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 7)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Neuronal Networks')
    plt.show()


# max: 82 - 2400
def plotNaiveBayes():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    z = np.array([
        [53, 45, 52, 53, 45, 52, 1],
        [55, 52, 44, 55, 52, 44, 1],
        [56, 55, 56, 56, 55, 56, 1],
        [57, 56, 57, 57, 56, 57, 1],
        [62, 61, 60, 62, 61, 60, 1],
        [68, 60, 69, 68, 60, 69, 1],
        [72, 68, 65, 72, 68, 65, 1],
        [75, 76, 59, 75, 76, 59, 1],
        [75, 82, 76, 75, 82, 76, 1],
        [75, 79, 76, 75, 79, 76, 1]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Naïve Bayes')
    plt.show()


# max: 86 - 2700
def plotAdaptativeBoosting():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    z = np.array([
        [53, 45, 52, 53, 45, 52, 1],
        [55, 52, 44, 55, 52, 44, 1],
        [56, 55, 56, 56, 55, 56, 1],
        [57, 56, 57, 57, 56, 57, 1],
        [62, 61, 60, 62, 61, 60, 1],
        [68, 60, 69, 68, 60, 69, 1],
        [72, 68, 65, 72, 68, 65, 1],
        [75, 76, 59, 75, 76, 59, 1],
        [75, 82, 76, 75, 82, 76, 1],
        [75, 79, 76, 75, 79, 76, 1]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Adaptative Boosting')
    plt.show()


# max: 80 - 2900
def plotRandomForest():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    z = np.array([
        [53, 45, 52, 53, 45, 52, 1],
        [55, 52, 44, 55, 52, 44, 1],
        [56, 55, 56, 56, 55, 56, 1],
        [57, 56, 57, 57, 56, 57, 1],
        [62, 61, 60, 62, 61, 60, 1],
        [68, 60, 69, 68, 60, 69, 1],
        [72, 68, 65, 72, 68, 65, 1],
        [75, 76, 59, 75, 76, 59, 1],
        [75, 82, 76, 75, 82, 76, 1],
        [75, 79, 76, 75, 79, 76, 1]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Random Forest')
    plt.show()


# max: 84 - 2700
def plotDecisionTree():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    z = np.array([
        [53, 45, 52, 53, 45, 52, 1],
        [55, 52, 44, 55, 52, 44, 1],
        [56, 55, 56, 56, 55, 56, 1],
        [57, 56, 57, 57, 56, 57, 1],
        [62, 61, 60, 62, 61, 60, 1],
        [68, 60, 69, 68, 60, 69, 1],
        [72, 68, 65, 72, 68, 65, 1],
        [75, 76, 59, 75, 76, 59, 1],
        [75, 82, 76, 75, 82, 76, 1],
        [75, 79, 76, 75, 79, 76, 1]
    ])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy', title='Decision Tree')
    plt.show()


plotNeuronalNetworks()
# plotNaiveBayes()
# plotAdaptativeBoosting()
# plotRandomForest()
# plotDecisionTree()
