import tkinter as tk

class MyGui:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("SYSC2010")
        self.window.geometry("500x500")
        self.x = ''
        self.y = ''
        self.csv = ''

        # CSV label and input
        tk.Label(self.window, text="CSV File name", font=('Arial', 12)).pack(padx=20, pady=5)
        self.textbox_CSV = tk.Text(self.window, height=1, font=('Arial', 12))
        self.textbox_CSV.pack(padx=20)

        # x-axis label and input
        tk.Label(self.window, text="X-axis Column name", font=('Arial', 12)).pack(padx=20, pady=5)
        self.textbox_x = tk.Text(self.window, height=1, font=('Arial', 12))
        self.textbox_x.pack(padx=20)

        # y-axis label and input
        tk.Label(self.window, text="Y-axis Column name", font=('Arial', 12)).pack(padx=20, pady=5)
        self.textbox_y = tk.Text(self.window, height=1, font=('Arial', 12))
        self.textbox_y.pack(padx=20)

        # Load button
        tk.Button(self.window, text="Load & Plot",
                  font=('Arial', 12),
                  command=self.load_data).pack(pady=10)

    def load_data(self):
        self.csv = self.textbox_CSV.get("1.0", "end-1c")
        self.x = self.textbox_x.get("1.0", "end-1c")
        self.y = self.textbox_y.get("1.0", "end-1c")
        self.window.destroy()


gui = MyGui()
gui.window.mainloop()

print(gui.csv)
