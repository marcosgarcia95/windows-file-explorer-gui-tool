import tkinter as tk

class RenameApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

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

def rename_func():
    root_app = tk.Tk()
    RenameApp(root_app)
    
    rename_app = RenameApp(root_app)
    rename_app.mainloop()