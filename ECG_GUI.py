import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MyGui:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SYSC2010")
        self.window.geometry("500x500")

        # CSV label and input
        self.label_CSV = tk.Label(self.window, text="CSV File name", font=('Arial', 12))
        self.label_CSV.pack(padx=20, pady=5)

        self.textbox_CSV = tk.Text(self.window, height=1, font=('Arial', 12))
        self.textbox_CSV.pack(padx=20)

        # x-axis label and input
        self.label_x = tk.Label(self.window, text="X-axis Column name", font=('Arial', 12))
        self.label_x.pack(padx=20, pady=5)

        self.textbox_x = tk.Text(self.window, height=1, font=('Arial', 12))
        self.textbox_x.pack(padx=20)

        # y-axis label and input
        self.label_y = tk.Label(self.window, text="Y-axis Column name", font=('Arial', 12))
        self.label_y.pack(padx=20, pady=5)

        self.textbox_y = tk.Text(self.window, height=1, font=('Arial', 12))
        self.textbox_y.pack(padx=20)

        # Load button
        self.button = tk.Button(self.window, text="Load & Plot", font=('Arial', 12))
        self.button.pack()

gui = MyGui()
gui.window.mainloop()


# read csv file from textbox_CSV
def read_csv_file(self):
    file_name = self.textbox_CSV.get("1.0", tk.END).strip()
    data = pd.read_csv(file_name)
    return data
MyGui.read_csv_file = read_csv_file
# plot data from csv file using matplotlib
def plot_data(self):
    data = self.read_csv_file()
    x_col = self.textbox_x.get("1.0", tk.END).strip()
    y_col = self.textbox_y.get("1.0", tk.END).strip()

    plt.figure()
    plt.plot(data[x_col], data[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col}")
    plt.show()
MyGui.plot_data = plot_data
# bind plot_data function to button
MyGui.button.config(command=MyGui.plot_data)
