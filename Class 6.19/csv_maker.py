import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

save_path = filedialog.asksaveasfilename(initialdir = ".", title = "Select csv destination file")
print(save_path)

row_index = 1
col_index = 1
with open(save_path, "w") as out_file:
    while True:
        cell_val = input(f"input value at row:{row_index} column:{col_index} (blank for new line, \"quit\" to quit):")
        if cell_val == "quit":
            break
        elif cell_val == "":
            out_file.write("\n")
            row_index = row_index + 1
            col_index = 1
        else:
            out_file.write("\"" + cell_val + "\",")
            col_index = col_index + 1

