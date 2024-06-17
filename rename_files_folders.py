import tkinter as tk
from tkinter import *

class RenameApp():
    def __init__(self):
        super().__init__()
        # self.grid()

        self.entrythingy = tk.Label(text="Welcome to the File/Folder Rename Application!",font= (0,17))
        self.entrythingy.grid(column=0, row=0)

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