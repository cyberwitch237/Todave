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

        # Get info From database // THIS CURRENTLY IS A TEMP MATRIX TO STORE VALUES, LATER MATRIX VALUES SHOULD BE DEPENDANT ON DATABASE
        def GetModuleData():
            global ModuleData
            global InstructorAvalibilities

            #Module Data = Module1, Module2, Module3, ..., Modulen
            #Modulen = Name, Code, Instructor(name and number), LectureInfo(list), PracticalInfo(list), TutorialInfo(list),
            #Lect/Pract/Tutinfo = Amount, Length

            #InstructorAvalibility = instructor1, instructor2, ..., instructorn
            #Instructorn = Monday, Tuesay, ..., Friday 
            #Days of the week = 9 - 10, 10 - 11, ..., 17 - 18 (im assuming the earliest a lecture can start is 09:00, latest a module can end is 18:00)


            ModuleData = [['Problem Solving and Computer Programming', 'CSC-10084', ['Bappaditya Mandal', 0], [1,2], [1,2], [0,0], ]] 
            InstructorAvalibilities = [[[True, True, True, True, True, True, True, True, False], [True, True, True, True, True, True, True, True, False], [True, True, True, True, True, True, True, True, False], [True, True, True, True, True, True, True, True, False], [True, True, True, True, True, True, True, True, False]]]
        
        # Generate the timetable

        GetModuleData()

        def Optimist(MODULEDATA, USERINPUT):

            global ModuleOutput
            global InstructorAvalibilities
            ModuleOutput = []

            #Timtable Output = Module1, Module2, Module3 ,..., Modulen
            #Modulen = Name, Code, Instructor, LectureInfo, PracticalInfo, TutorialInfo, 
            #Lect/pract/tutInfo = Lecture1, Lecture2
            #Lect/pract/tutn = Day, Hour(s)

            for i in range(len(MODULEDATA)): #Create Every Module Output
                NewModule = []
                NewModule.append(ModuleData[i][0])
                NewModule.append(ModuleData[i][1])
                NewModule.append(ModuleData[i][2][0])

                lecturelength = ModuleData[i][3][1]
                InstructorNumnber = ModuleData[i][2][1]
                for i in range(ModuleData[i][3][0]): #Create Every Lecture for the Module
                    day = 0
                    time = USERINPUT[0] - 9
                    DayCheckingList = InstructorAvalibilities[InstructorNumnber][day]
                    print(DayCheckingList)

                    while all(DayCheckingList[time:(time + lecturelength - 1)]) == False: # check if there is a slot avalible for lecture on current day
                        print('idfk')

                    print(day)
                    print(time)

                ModuleOutput.append(NewModule)

            print(ModuleOutput)


        # Show info on the generated timetable


        # User interface
        TimetableUserInputs = [11]

        #GenerateUserInputs = Best start time, 

        

        self.Optimistsort = ttk.Button(self.master, text = 'Optimist', width=40, command=lambda : Optimist(ModuleData, TimetableUserInputs))
        self.Optimistsort.pack()
    
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

