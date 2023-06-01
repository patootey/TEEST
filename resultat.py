import pandas as pd
import matplotlib.pyplot as plt
import re

data = []
tid = 0
tid_array = []
al_array = []
velocity = 0
velocity_array = []

with open("data.txt", newline="", encoding="utf-8") as txtfile:
    reader = pd.read_csv(txtfile, sep=",", header=None)
    for i, row in reader.iterrows():
        data.append(row.values.tolist())
        acceleration_str = re.sub(
            r"[^0-9.]", "", row[0]
        )  # Remove non-numeric characters from the string
        acceleration = (float(acceleration_str) / 1000 * 9.81 - 10) * -1
        al_array.append(acceleration)

for i in al_array:
    tid += 0.1
    tid_array.append(tid)
    velocity += i * 0.1
    velocity_array.append(velocity)

print(velocity_array)
plt.plot(tid_array, velocity_array)
plt.show()

print(al_array.index(0.2684800000000003))


def Cd():
    return drag() / (0.5 * 1.293 * velocity_array[48] * 0.3472)


def drag():
    return al_array[48] * 0.076 - 9.81 * 0.076


print(Cd())
