from signal import signal
import ECG_GUI
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ECG_GUI.gui.csv
ECG_GUI.gui.csv

data = pd.read_csv(ECG_GUI.gui.csv)

time = pd.to_datetime(data['t']) # unreadable otherwise
lead_original = data['lead_I']

# remove anomolous samples
# time = time[200:-80]
# lead = lead[200:-80]

# olot first 1000 samples of subset
# time = time[250:1250]
# lead = lead[250:1250]

mean = np.mean(lead_original)

# subtract mean from signal
lead_processed = lead_original - mean

signal = np.convolve(lead_processed,np.ones(100)/100,mode='same')


# temp vs time
plt.figure()
plt.plot(time, signal)
plt.plot(time, lead_original)
plt.xlabel(ECG_GUI.gui.x)
plt.ylabel(ECG_GUI.gui.y)
plt.title("Lead I vs Time")
#plt.xticks(rotation=45)
plt.show()