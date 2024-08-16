import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.49, 2.58, 3.587, 4.587, 5.587])
y = np.array([0.00081, 0.08833, 0.1849, 0.2827, 0.381])
             

plt.xlabel("Voltage")
plt.ylabel("Current")

plt.plot(x, y)
plt.show()