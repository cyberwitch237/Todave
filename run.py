from tkinter import *
from tkinter import ttk

import sv_ttk #changes tkinter to look like windows 11, pip install sv-ttk

def RetrieveModuleData() -> None: #temporary, currently takes from txt files, can be replaced with sql stuff later. #for generating timetables

    print("Getting Module Data")

    global ModuleName
    global ModuleCode
    global LeadStaff
    global LectureLength
    global TutorialLength
    global LectureAmount
    global TutorialAmount
    global Optional
    global Monday
    global Tuesday
    global Wednesday
    global Thursday
    global Friday

    with open("Cashe/SharedFiles/ModuleNames.txt", 'r') as file:
        ModuleName = file.read().splitlines()

    with open("Cashe/SharedFiles/ModuleCodes.txt", 'r') as file:
        ModuleCode = file.read().splitlines()

    with open("Cashe/SharedFiles/LeadStaff.txt", 'r') as file:
        LeadStaff = file.read().splitlines()

    with open("Cashe/SharedFiles/LectureLength.txt", 'r') as file:
        LectureLength = file.read().splitlines()

    with open("Cashe/SharedFiles/TutorialLength.txt", 'r') as file:
        TutorialLength = file.read().splitlines()

    with open("Cashe/SharedFiles/LectureAmount.txt", 'r') as file:
        LectureAmount = file.read().splitlines()

    with open("Cashe/SharedFiles/TutorialAmount.txt", 'r') as file:
        TutorialAmount = file.read().splitlines()

    with open("Cashe/SharedFiles/Optional.txt", 'r') as file:
        Optional = file.read().splitlines()
    
    with open("Cashe/SharedFiles/Monday.txt", 'r') as file:
        Monday = file.read().splitlines()

    with open("Cashe/SharedFiles/Tuesday.txt", 'r') as file:
        Tuesday = file.read().splitlines()

    with open("Cashe/SharedFiles/Wednesday.txt", 'r') as file:
        Wednesday = file.read().splitlines()

    with open("Cashe/SharedFiles/Thursday.txt", 'r') as file:
        Thursday = file.read().splitlines()

    with open("Cashe/SharedFiles/Friday.txt", 'r') as file:
        Friday = file.read().splitlines()

    print(ModuleName)
    print(ModuleCode)
    print(LeadStaff)
    print(LectureLength)
    print(TutorialLength)
    print(LectureAmount)
    print(TutorialAmount)
    print(Optional)
    print(Monday)
    print(Tuesday)
    print(Wednesday)
    print(Thursday)
    print(Friday)


    global NumberOfModules
    NumberOfModules = len(ModuleCode)

    print(str(NumberOfModules) + " Modules")

def Optimist() -> None:
    CurrentModule = 0

    for i in range (NumberOfModules): 
        print("test")

        if Monday[CurrentModule] == 'True':
            print("Monday is true")

        CurrentModule = CurrentModule + 1


def CreateTimetable() -> None:

    RetrieveModuleData()

    Optimist()

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
        self.Testbutton = ttk.Button(self.master, text = 'Testbutton', width=20, command = CreateTimetable)
        self.Testbutton.pack()
        
        # Show info on the generated timetable
    
    def GoBack(self) -> None:
        self.PageStack.pop()

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

