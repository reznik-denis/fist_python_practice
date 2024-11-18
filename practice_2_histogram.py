import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'serif','color':'blue','size':10}
font2 = {'family':'serif','color':'darkred','size':10}

x = np.array([99, 86, 87, 88, 68, 68, 75, 100, 86, 100, 87, 94, 78, 77, 85, 86, 94, 57])

plt.hist(x, color = "red")
plt.grid(axis = 'y', color = 'red', linestyle = '--', linewidth = 0.5)

plt.xlabel("Відсоток", fontdict = font1)
plt.ylabel("Значення", fontdict = font2)

plt.suptitle("Якість продукту")

plt.show()