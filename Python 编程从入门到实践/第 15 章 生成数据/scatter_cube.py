import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)


#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()