from tkinter import *
from tkinter import ttk

import sv_ttk #changes tkinter to look like windows 11, pip install sv-ttk

class app: #each page of the app is a function under this class
    
    def __init__(self, master):
        self.master = master
        self.MainMenu()
    
    def MainMenu(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.ModulesButton = ttk.Button(self.master, text='Create Modules', width=20, command=self.CreateModules)
        self.GenTimeables = ttk.Button(self.master, text='Generate Timetable', width=20)

        self.ModulesButton.grid(row=0, column=0, padx=5, pady=5)
        self.GenTimeables.grid(row=1, column=0, padx=5, pady=5)
    
    def CreateModules(self):
        for i in self.master.winfo_children():
            i.destroy()

root = Tk()
app(root)

sv_ttk.set_theme("dark")

root.mainloop()

