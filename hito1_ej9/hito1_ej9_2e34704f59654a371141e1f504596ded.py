#Sistema de Ecuaciones
import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(0, 9, 100)
plt.plot(
    x, np.exp(x / 3) * np.cos(x) + 10 * np.sin(3 * x), 
    x, x ** 2 / 4
)
plt.show()      