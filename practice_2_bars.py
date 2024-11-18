import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'serif','color':'blue','size':10}
font2 = {'family':'serif','color':'darkred','size':10}

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 7, 1, 10])

plt.subplot(1, 2, 1)
plt.barh(x, y, color = "red")

plt.grid(axis = 'x', color = 'red', linestyle = '--', linewidth = 0.5)

plt.xlabel("Відсоток", fontdict = font1)
plt.ylabel("Значення", fontdict = font2)

x = np.array(["A", "B", "C", "D"])
y = np.array([5, 18, 23, 19])

plt.subplot(1, 2, 2)
plt.bar(x, y, color = "green")

plt.grid(axis = 'y', color = 'green', linestyle = ':', linewidth = 0.5)

plt.xlabel("Відсоток", fontdict = font1)
plt.ylabel("Значення", fontdict = font2)

plt.suptitle("Якість продукту")

plt.subplots_adjust(wspace=0.3)

plt.show()