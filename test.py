import numpy as np
import matplotlib.pyplot as plt


class Test:
    def __init__(self):
        self.coeff = 0.2
        self.gravity = 9.8
        self.times = np.linspace(0, 3.5, 100)
        self.times_step = (max(self.times) - min(self.times)) / len(self.times)
        self.no_drag_velocities = self.gravity * self.times
        self.a = 0
        self.v = 0
        self.drag_velocities = []


test = Test()

for i in test.times:
    test.drag_velocities.append(test.v)
    test.a = test.gravity - test.coeff * test.v**2 * test.times_step
    test.v = test.v + test.a * test.times_step

plt.plot(test.times, test.no_drag_velocities, label="Without Drag")
plt.plot(test.times, test.drag_velocities, label="With Drag")
plt.xlabel("Time [s]")
plt.ylabel("Speed [m/s]")
plt.legend(loc="upper left")
plt.grid()
plt.show()
