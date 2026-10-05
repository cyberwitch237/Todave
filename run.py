import tkinter as Tk
from tkinter import ttk

import sv_ttk #changes tkinter to look like windows 11, pip install sv-ttk

root = Tk.Tk()

Button1 = ttk.Button(root, text='Create Modules', width=20)
Button1.grid(row=0, column=0, padx=5, pady=5)

Button2 = ttk.Button(root, text='Generate Timetable', width=20)
Button2.grid(row=1, column=0, padx=5, pady=5)

sv_ttk.set_theme("dark")

root.mainloop()