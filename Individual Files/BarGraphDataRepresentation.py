import numpy as np
import matplotlib.pyplot as plt

aluminum = np.array([6.4e-5, 3.01e-5, 2.36e-5, 3.0e-5, 7.0e-5, 4.5e-5, 3.8e-5, 4.2e-5, 2.62e-5, 3.6e-5])
copper = np.array([4.5e-5, 1.97e-5, 1.6e-5, 1.97e-5, 4.0e-5, 2.4e-5, 1.9e-5, 2.41e-5, 1.85e-5, 3.3e-5])
steel = np.array([3.3e-5, 1.2e-5, 0.9e-5, 1.2e-5, 1.3e-5, 1.6e-5, 1.4e-5, 1.58e-5, 1.32e-5, 2.1e-5])

# calculating the mean values of the material's thermal expansion coefficient
aluminum_mean = np.mean(aluminum)
copper_mean = np.mean(copper)
steel_mean = np.mean(steel)

materials = ['Aluminum', 'Copper', 'Steel']
x_pos = np.arange(len(materials))
CTEs = [aluminum_mean, copper_mean, steel_mean]

fig, ax = plt.subplots()

ax.bar(x_pos, CTEs, align='center', alpha=0.5)
ax.set_ylabel('Coefficient of Thermal Expansion (C^-1)')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials)
ax.set_title('Coefficient of Thermal Expansion (CTE) of Three Metals')
ax.yaxis.grid(True)

plt.tight_layout()
plt.savefig('bar_plot.png')
plt.show()