import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("volume.csv")

frequency = data["volume"]
time = data["time"]

plt.plot(frequency, time)
plt.xlabel("Volume (GB)")
plt.ylabel("Time (seconds)")
plt.title("Volume vs Time (1000 files)")
plt.xticks(frequency, fontsize=6)
plt.yticks(time, fontsize=6)
plt.grid(True)
plt.savefig("volume_plot.png")