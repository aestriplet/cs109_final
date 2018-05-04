import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

labels = ["men", "women"]
x_list = [25, 75 ]
colors = ["purple", "blue"]

plt.axis('equal')
plt.tight_layout()
plt.pie(x_list,
        labels = labels,
        colors = colors,
        autopct = '%.2f' )
plt.figure(2)
plt.show()
