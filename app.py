from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10) #sets the border from the frame of the app window to the first widget/label/button
frm.grid()
ttk.Label(frm, text="Welcome to the Windows File Explorer GUI tool!").grid(column=0, row=0, columnspan=3,)
ttk.Label(frm, text="Please select from the following options below.").grid(column=0, row=1, columnspan=3)
ttk.Button(frm, text="Rename Files/Folders",).grid(column=0, row=2)
ttk.Button(frm, text="Refresh Excel Files",).grid(column=1, row=2)
ttk.Button(frm, text="Placeholder here",).grid(column=2, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3, columnspan=3)
root.mainloop()