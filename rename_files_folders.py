import tkinter as tk
from tkinter import *
from pathlib import Path
import os
from tkinter import messagebox

class RenameApp():
    def __init__(self):
        super().__init__()
        # self.grid()

        self.introtext = tk.Label(text="Welcome to the File Rename Application!",font= (0,17))
        self.introtext.grid(column=0, row=0, columnspan=2)

        self.subtext = tk.Label(text="Please enter the absoluite path of where you want to rename your files")
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

        self.checkvarfilecheck = IntVar(value=1)
        self.checkvarfoldercheck = IntVar(value=1)

        self.filecheck = tk.Checkbutton(text = 'Rename Files?',onvalue=1, offvalue=0, variable=self.checkvarfilecheck).grid(column=0,row=6)
        self.foldercheck = tk.Checkbutton(text = 'Rename Folders?',onvalue=1, offvalue=0,variable=self.checkvarfoldercheck).grid(column=0,row=7)

        self.execute_button = tk.Button(text="Execute", command = lambda: [get_path(self.enterpath.get(), 
                                                                                   self.begstring_input.get(), 
                                                                                   self.endstring_input.get(),
                                                                                   self.checkvarfilecheck.get(),
                                                                                   self.checkvarfoldercheck.get())])
        self.execute_button.grid(column=0, row=8,columnspan=2)       

        self.return_button = tk.Button(text="Return to main menu", command = '')
        self.return_button.grid(column=0,row=9, columnspan=2) 

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
    #           self.contents.get()))

def rename_func(frame):
    # root = Tk() # first window
    # top = Toplevel(root)
    for widget in frame.winfo_children():
        widget.destroy()
    rename_app = RenameApp()
    # rename_app.mainloop()



def get_path(path, begstring, endstring, file_check,folder_check):
    win_path = fr'{path}'
    try:
        print(file_check,folder_check)
        for filename in os.listdir(win_path):
            if not os.path.exists(filename):
                if file_check ==1 and folder_check==1:
                    print(filename)
                    print(path+'\\'+filename)
                    print(begstring, endstring)
                    os.rename(path+'\\'+filename, path+'\\'+filename.replace(begstring, endstring))
                elif file_check ==1 and folder_check==0:
                    if os.path.isdir(path+'\\'+filename):
                         pass
                    else: 
                        os.rename(path+'\\'+filename, path+'\\'+filename.replace(begstring, endstring))
                elif file_check ==0 and folder_check ==1:
                    if os.path.isdir(path+'\\'+filename):
                        os.rename(path+'\\'+filename, path+'\\'+filename.replace(begstring, endstring))
                    else: 
                        pass
                else:
                    pass
        if file_check==1 or folder_check==1:
            popup_msg_success()
        else: 
            messagebox.showinfo(title="Did not run!", message = 'The script could not run. Please check one of the two boxes to replace a file or folder!')
    except:
                messagebox.showinfo(title="Error!", message = 'There was an error renaming your files!')


def popup_msg_success():
    messagebox.showinfo(title="Success!",message = 'The files were renamed with no issues!')

    # return win_path 