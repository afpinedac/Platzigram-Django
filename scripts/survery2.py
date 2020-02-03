from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

#max: 82 - 2700
def plotNeuronalNetworks():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    x = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
    y = np.array([[300, 300, 300], [600, 600, 600], [900, 900, 900], [1200, 1200, 1200], [1500, 1500, 1500], [1800, 1800, 1800], [2100, 2100, 2100], [2400, 2400, 2400], [2700, 2700, 2700], [2938, 2938, 2938]])
    z = np.array([[53, 45, 52], [55, 52, 44], [56, 55, 56], [57, 56, 57], [62, 61, 60], [68, 60, 69], [72, 68, 65], [75, 76, 59], [75, 82, 76 ], [75, 79, 76]])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy',  title='Neuronal Networks')
    plt.show()


#max: 82 - 2400
def plotNaiveBayes():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    x = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
    y = np.array([[300, 300, 300], [600, 600, 600], [900, 900, 900], [1200, 1200, 1200], [1500, 1500, 1500], [1800, 1800, 1800], [2100, 2100, 2100], [2400, 2400, 2400], [2700, 2700, 2700], [2938, 2938, 2938]])
    z = np.array([[52, 47, 49], [53, 48, 47], [55, 49, 51], [60, 52, 55], [64, 65, 66], [66, 67, 72], [73, 71, 69], [82, 77, 79], [81, 79, 78 ], [79, 77, 73]])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy',  title='Naïve Bayes')
    plt.show()

#max: 86 - 2700
def plotAdaptativeBoosting():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    x = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
    y = np.array([[300, 300, 300], [600, 600, 600], [900, 900, 900], [1200, 1200, 1200], [1500, 1500, 1500], [1800, 1800, 1800], [2100, 2100, 2100], [2400, 2400, 2400], [2700, 2700, 2700], [2938, 2938, 2938]])
    z = np.array([[55, 56, 57], [57, 58, 59], [61, 62, 58], [57, 61, 64], [66, 68, 70], [72, 73, 74], [77, 79, 81], [76, 69, 75], [81, 86, 84], [84, 85, 80]])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy',  title='Adaptative Boosting')
    plt.show()


#max: 80 - 2900
def plotRandomForest():
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    x = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
    y = np.array([[300, 300, 300], [600, 600, 600], [900, 900, 900], [1200, 1200, 1200], [1500, 1500, 1500], [1800, 1800, 1800], [2100, 2100, 2100], [2400, 2400, 2400], [2700, 2700, 2700], [2938, 2938, 2938]])
    z = np.array([[55, 56, 48], [59, 48, 56], [60, 57, 54], [60, 52, 55], [65, 67, 69], [71, 69, 68], [72, 70, 72], [69, 71, 75], [78, 79, 78 ], [78, 77, 80]])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy',  title='Random Forest')
    plt.show()


#max: 84 - 2700
def plotDecisionTree():

    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_xlim([1, 3])
    ax.set_ylim([0, 3000])
    ax.set_zlim([0, 100])

    x = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
    y = np.array([[300, 300, 300], [600, 600, 600], [900, 900, 900], [1200, 1200, 1200], [1500, 1500, 1500], [1800, 1800, 1800], [2100, 2100, 2100], [2400, 2400, 2400], [2700, 2700, 2700], [2938, 2938, 2938]])
    z = np.array([[48, 51, 55], [53, 62, 58], [56, 56, 51], [59, 58, 62], [63, 64, 66], [70, 67, 72], [73, 71, 69], [68, 76, 79], [83, 82, 84], [81, 79, 81]])

    ax.view_init(elev=30, azim=220)

    plt.xticks([i for i in range(1, 4)])
    plt.yticks([i for i in range(0, 3000, 300)])

    ax.plot_surface(x, y, z)
    ax.set(xlabel='Month', ylabel='Students', zlabel='Accuracy',  title='Decision Tree')
    plt.show()


plotNeuronalNetworks()
plotNaiveBayes()
plotAdaptativeBoosting()
plotRandomForest()
plotDecisionTree()
