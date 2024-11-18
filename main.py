import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["Яблука", "Банани", "Вишні", "Картопля"]

plt.pie(y, labels = my_labels)
plt.legend(title = "Продукти:", loc="best", bbox_to_anchor=(0.95, 0.5))
plt.tight_layout()

plt.suptitle("Залишок продуктів на складі")

plt.show()