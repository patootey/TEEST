import pandas as pd
import matplotlib.pyplot as plt
import re

def main():
    data = []
    time = 0
    time_array = []
    acceleration_array = []
    velocity = 0
    velocity_array = []

    # Read data from text file
    with open("Prosjekt_Fritt_Fall_Data.txt", newline="", encoding="utf-8") as txtfile:
        reader = pd.read_csv(txtfile, sep=",", header=None)

        # Process each row in the data
        for i, row in reader.iterrows():
            data.append(row.values.tolist())
            acceleration_str = re.sub(
                r"[^0-9.]", "", row[0]
            )  # Remove non-numeric characters from the string
            acceleration = (float(acceleration_str) / 1000 * 9.81 - 10) * -1
            acceleration_array.append(acceleration)

    # Append velocity and time values to their respective arrays
    for i in acceleration_array:
        time += 0.1
        time_array.append(time)
        velocity += i * 0.1
        velocity_array.append(velocity)
    plt.plot(time_array, velocity_array, label="Microbit result")