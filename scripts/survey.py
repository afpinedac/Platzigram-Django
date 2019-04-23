import matplotlib.pyplot as plt
import numpy as np

"""
1) REASON
"""

plt.rcdefaults()
plt.figure(figsize=(15, 7))
objects = ('Other(s) reason(s)', 'I did an assignment \n(or several) with one or \n more partners and then \nthey sent me the code',
           'Get good grades in the \n assignments', 'I did not have enough time', 'I was not able to do \n some assignment \n(or several)')
y_pos = np.arange(len(objects))
performance = [8, 20, 4, 19, 15]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects, fontsize=16)
# plt.xlabel('Usage')
plt.title('What was the reason for copying?', fontdict={'fontsize': 20, 'fontweight': 'medium'})

plt.show()

"""
2) SECOND QUESTION - THE STUDENT WAS AFFECTED
"""

plt.figure(figsize=(7, 7))

# Data to plot
labels = 'It affected me a lot', 'It affected me a little bit', 'It did not affect me', 'It helped me a little bit', 'It helped me a lot'
sizes = [2, 7, 15, 6, 0]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'LightSeaGreen']
explode = [0.05] * 5  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title('Do you feel that having copied affected your learning \n of the topics and consequently your qualification in the exam?')
plt.show()

"""
3) THIRD QUESTION - WOULD COPY AGAIN
"""

plt.figure(figsize=(7, 7))
# Data to plot
labels = 'Most probably', 'Probably', 'I am not sure', 'Improbably', 'Very unlikely'
sizes = [1, 6, 11, 9, 3]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'LightSteelBlue']
explode = [0.05] * 5  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title('Assuming that I would never have known about the copy, and you would not \n have received this email, would you still copy in the rest of the course?')
plt.show()
