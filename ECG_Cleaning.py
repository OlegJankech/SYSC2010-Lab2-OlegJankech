import ECG_GUI
import pandas as pd
import matplotlib as plt

data = pd.read_csv(ECG_GUI.gui.csv)


time = pd.to_datetime(data['t']) # unreadable otherwise
temp = data['temperature_C']
humidity = data['humidity_pct']

# temp vs time
plt.figure()
plt.plot(time, temp)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Time")
plt.xticks(rotation=45)