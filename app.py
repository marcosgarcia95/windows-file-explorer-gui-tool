from tkinter import *
from tkinter import ttk
if __package__ is None or __package__ == '':
    # uses current directory visibility
    import rename_files_folders as rn
else:
    # uses current package visibility
    from . import rename_files_folders as rn

root = Tk() # first window

frm = ttk.Frame(root, padding=10) #sets the border from the frame of the app window to the first widget/label/button
frm.grid()
ttk.Label(frm, text="Welcome to the Windows File Explorer GUI tool!",font= (0,17)).grid(column=0, row=0, columnspan=3, )
ttk.Label(frm, text="Please select from the following options below.").grid(column=0, row=1, columnspan=3)
ttk.Button(frm, text="Rename Files/Folders",command=lambda: rn.rename_func(frm)).grid(column=0, row=2)
ttk.Button(frm, text="Refresh Excel Files").grid(column=1, row=2)
ttk.Button(frm, text="Placeholder here",).grid(column=2, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3, columnspan=3)








root.mainloop()

