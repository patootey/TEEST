import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt')
t = data[:, 0]
k = data[:, 1]

x = [k_val for k_val, count in t]
y = [count for k_val, count in k]

plt.plot(x, y, 'r-')
plt.title('Sjanse terningspill')
plt.xlabel('Antall terninger kastet')
plt.ylabel('Antall duplikate resultater')
plt.grid()