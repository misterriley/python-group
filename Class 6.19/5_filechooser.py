from tkinter import filedialog

import tkinter as tk

root = tk.Tk()
root.withdraw()

save_path = filedialog.asksaveasfilename(initialdir = ".", title = "Your title goes here")
print(save_path)
