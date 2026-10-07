from tkinter import *
from tkinter import ttk

import sv_ttk #changes tkinter to look like windows 11, pip install sv-ttk

class app: #each page of the app is a function under this class
    
    def __init__(self, master):
        self.master = master
        self.MainMenu()
        self.PageStack = [] # Stack used for returning to previous pages easily

    # Clears the screen
    def _ClearAll(self) -> None:
        for i in self.master.winfo_children():
            i.destroy() 
    
    # Adds a back button to the current page
    def _CreateBackButton(self) -> ttk.Button:
        self.BackButton = ttk.Button(self.master, text = "Back", width = 10, command = self.GoBack)
        self.BackButton.pack(side=BOTTOM, anchor="sw", padx=10, pady=10)
    
    # Clears the screen and creates a new page, appended to the page stack
    def _NewPage(self, func: callable) -> None:
        self._ClearAll()
        self._CreateBackButton()
        self.PageStack.append(func)
        print("appended")
        print(len(self.PageStack))
    
    # Go to main menu
    def MainMenu(self) -> None:
        self._ClearAll()

        # Create option butttons
        self.ModulesButton = ttk.Button(self.master, text = 'Create Modules', width=20, command = self.CreateModules)
        self.GenTimeables = ttk.Button(self.master, text = 'Generate Timetables', width=20, command = self.GenerateTimetables)

        # Position option buttons
        self.ModulesButton.grid(row=0, column=0, padx=15, pady=15)
        self.GenTimeables.grid(row=1, column=0, padx=15, pady=15)

        # Configure column
        root.columnconfigure(0, weight=1)
    
    # Go to modules page
    def CreateModules(self) -> None:
        self._NewPage(self.CreateModules)
    
    # Go to timetables page
    def GenerateTimetables(self) -> None:
        self._NewPage(self.GenerateTimetables)
        
        # Generate the timetable
        
        # Show info on the generated timetable
    
    def GoBack(self) -> None:
        bob = self.PageStack.pop()

        max_index = len(self.PageStack)
        print(max_index)
        if max_index > 0:
            # Go to previous page
            self.PageStack[max_index](self)
        else:
            # Go to main menu
            self.MainMenu()



# Initialise window
root = Tk()
app(root)
root.minsize(600, 600)

sv_ttk.set_theme("dark")

root.mainloop()

