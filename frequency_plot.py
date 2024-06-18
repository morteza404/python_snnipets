import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("frequency.csv")

frequency = data["frequency"]
time = data["time"]

plt.plot(frequency, time)
plt.xlabel("Frequency")
plt.ylabel("Time(seconds)")
plt.title("Frequency vs Time")
plt.xticks(frequency, fontsize=6)
plt.yticks(time, fontsize=6)
plt.grid(True)
plt.savefig("frequency_plot.png")
