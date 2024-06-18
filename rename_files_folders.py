import tkinter as tk
from tkinter import *

class RenameApp():
    def __init__(self):
        super().__init__()
        # self.grid()

        self.introtext = tk.Label(text="Welcome to the File/Folder Rename Application!",font= (0,17))
        self.introtext.grid(column=0, row=0, columnspan=2)

        self.subtext = tk.Label(text="Please enter the absoluite path of where you want to rename your files and folders")
        self.subtext.grid(column= 0, row=1, columnspan=2)

        self.exampletext = tk.Label(text ="An example -  C:\\Users\\gama6p9\\Downloads")
        self.exampletext.grid(column = 0, row=2, columnspan=2)

        self.exampletext = tk.Label(text ="File Path Here:")
        self.exampletext.grid(column = 0, row=3)
        
        self.enterpath = tk.Entry(width=50)
        self.enterpath.grid(column = 1, row = 3)

        self.begstring = tk.Label(text ="What text do you want to rename?")
        self.begstring.grid(column = 0, row=4)
        
        self.begstring_input = tk.Entry(width=50)
        self.begstring_input.grid(column = 1, row = 4)        

        self.endstring = tk.Label(text ="What do you want to replace it with?")
        self.endstring.grid(column = 0, row=5)
        
        self.endstring_input = tk.Entry(width=50)
        self.endstring_input.grid(column = 1, row = 5)    


        self.execute_button = tk.Button(text="Execute")
        self.execute_button.grid(column=0, row=6,columnspan=2)       

        self.return_button = tk.Button(text="Return to main menu")
        self.return_button.grid(column=0,row=7, columnspan=2) 

        # Create the application variable.
        # self.contents = tk.StringVar()
        # Set it to some value.
        # self.contents.set()
        # # Tell the entry widget to watch this variable.
        # self.entrythingy["textvariable"] = self.contents

    #     # Define a callback for when the user hits return.
    #     # It prints the current value of the variable.
    #     self.entrythingy.bind('<Key-Return>',
    #                          self.print_contents)

    # def print_contents(self, event):
    #     print("Hi. The current entry content is:",
    #           self.contents.get())

def rename_func(frame):
    # root = Tk() # first window
    # top = Toplevel(root)
    for widget in frame.winfo_children():
        widget.destroy()
    rename_app = RenameApp()
    # rename_app.mainloop()