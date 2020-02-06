import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# plt.figure(figsize=(3, 4))


df = pd.read_csv('C:\\xampp2\\htdocs\\ticademia2\\storage\\app\\research\\xxx2.csv', sep=',', header=None)
file_data = [tuple(x) for x in df.values]

"""
    [0] user_id
    [1] user_document
    [2] survey_q1   // las retroalimentaciones fueron acertadas
    [3] survey_q2   // seguias o nó la retroalimentación
    [4] unal_score
    [5] ticademia_tries_ratio
"""


def diagram1():
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


def diagram2():
    data_survey_q1 = [i[2] for i in file_data]
    data_survey_q2 = [i[3] for i in file_data]
    data_unal_score = [float(i[4]) for i in file_data]
    data_ticademia_tries_ratio = [i[5] for i in file_data]

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

    # plt.axis([0, 5.5, 0, 11])
    plt.xlabel('Feedback acceptance response')
    plt.ylabel('Course score')
    plt.xticks([i for i in range(1, 6)])
    plt.grid(True)
    # plt.legend(numpoints=1)
    # plt.legend(loc='upper left', prop={'size': 9})
    plt.title('Feedback acceptance / Course score')
    plt.figure(figsize=(10, 8))
    plt.show()

    for cluster, cluster_data in clusters.items():
        print("cluster={} <<>> avg={} <<>> n={}".format(cluster_data['description'], str(clusters[cluster]['avg']), len(clusters[cluster]['data'])))
        print("{}".format(str(clusters[cluster]['stats'])))

    # print notes in cluster


def diagram3():
    data_survey_q1: list = [i[0] for i in file_data]
    data_survey_q2: list = [i[1] for i in file_data]

    data_survey_q1.pop(0)
    data_survey_q2.pop(0)


    # data to plot
    n_groups = 5
    means_frank = (
        data_survey_q1.count('1'),
        data_survey_q1.count('2'),
        data_survey_q1.count('3'),
        data_survey_q1.count('4'),
        data_survey_q1.count('5')
    )
    means_guido = (
        data_survey_q2.count('1'),
        data_survey_q2.count('2'),
        data_survey_q2.count('3'),
        data_survey_q2.count('4'),
        data_survey_q2.count('5')
    )

    sum_q1 = sum(means_frank)
    sum_q2 = sum(means_guido)

    percentages = (
        means_frank[0] / sum_q1 * 100,
        means_frank[1] / sum_q1 * 100,
        means_frank[2] / sum_q1 * 100,
        means_frank[3] / sum_q1 * 100,
        means_frank[4] / sum_q1 * 100,

        means_guido[0] / sum_q2 * 100,
        means_guido[1] / sum_q2 * 100,
        means_guido[2] / sum_q2 * 100,
        means_guido[3] / sum_q2 * 100,
        means_guido[4] / sum_q2 * 100,
    )

    print(percentages)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, means_frank, bar_width,
                     alpha=opacity,
                     color='b',
                     label='PQ1')

    rects2 = plt.bar(index + bar_width, means_guido, bar_width,
                     alpha=opacity,
                     color='r',
                     label='PQ2')

    title_font = {'fontname': 'Arial', 'size': '8.5', 'color': 'black', 'weight': 'normal'}
    for k, rect in enumerate(rects1 + rects2):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "{0:.2f}%".format(float(percentages[k])) , ha='center', va='bottom', **title_font)

    plt.xlabel('Response')
    plt.ylabel('Occurrences')
    plt.title('Survey responses')
    plt.xticks(index + bar_width - 0.2, ('1', '2', '3', '4', '5'))
    plt.legend()

    plt.tight_layout()
    plt.show()


diagram3()

# diagram1()
# diagram2()
