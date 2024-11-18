import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])
y2_points = np.array([5, 4, 8, 2])

plt.subplot(1, 2, 1)
plt.plot(y_points, ls = '--', c = 'r', linewidth = '3')
plt.plot(y2_points, ls = ':', c = 'g', linewidth = '3')

font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'darkred','size':10}

plt.title("Продуктивність роботи", fontdict = font1)
plt.xlabel("Відсоток продуктивності", fontdict = font2)
plt.ylabel("Робочі години", fontdict = font2)

plt.grid(color = 'green', linestyle = ':', linewidth = 1)

x = np.array([0, 0.1, 0.2, 0.3, 0.6])
y = np.array([10, 15, 20, 25, 30])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.title("Зростання доходу", fontdict = font1)
plt.xlabel("Дні місяця", fontdict = font2)
plt.ylabel("Відсоток зростання", fontdict = font2)

plt.grid(color = 'green', linestyle = ':', linewidth = 1)

plt.suptitle("Залежність доходу від продуктивності")

plt.subplots_adjust(wspace=0.5)

plt.show()