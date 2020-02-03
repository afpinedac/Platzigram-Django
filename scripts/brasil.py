import matplotlib.pyplot as plt

# Plot a line graph

axes = plt.axes()
axes.set_xlim([1, 10])

plt.plot([0, 5, 15, 12, 14, 42, 34, 78, 65, 67, 12], label='Neuronal Networks')
plt.plot([0, 16, 35, 12, 14, 52, 64, 64, 72, 82, 90], label='Naïve Bayes')
plt.plot([0, 54, 12, 82, 75, 23, 86, 61, 45, 26, 12], label='Adaptative Boosting')
plt.plot([0, 53, 45, 32, 21, 78, 98, 58, 41, 88, 21], label='Random Forest')
plt.plot([0, 0, 87, 78, 67, 34, 100, 68, 26, 63, 3], label='Decision Trees')

# Add labels and title
plt.title("Overall Accuracy")
plt.xlabel("Dataset")
plt.ylabel("Accuracy")


plt.legend()

plt.show()
