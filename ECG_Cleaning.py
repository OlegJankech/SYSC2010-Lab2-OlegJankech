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
lead_processed = lead_original

signal = np.convolve(lead_processed,np.ones(20)/20,mode='same')

# save processed data to new csv without date
processed_data = pd.DataFrame({'t': data['t'], 'lead_I': signal})
processed_data.to_csv('processed_ecg.csv', index=False)

time = time[250:750]
lead_original = lead_original[250:750]
signal = signal[250:750]

# temp vs time
plt.figure()
plt.plot(data['t'][250:750], lead_original)
plt.plot(data['t'][250:750], signal)
plt.xlabel(ECG_GUI.gui.x)
plt.ylabel(ECG_GUI.gui.y)
plt.title("Processed and Unprocessed Lead I")
plt.xticks(rotation=45)
plt.show()