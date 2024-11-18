import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86, 94, 57])
colors = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])

font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'darkred','size':10}

plt.title("Відвідуваність", fontdict = font1)
plt.xlabel("Дні місяця", fontdict = font2)
plt.ylabel("Кількість працівників", fontdict = font2)

plt.scatter(x, y, c=colors, cmap='rainbow_r')

plt.colorbar()

plt.show()