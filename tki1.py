from tkinter import *
a=Tk()
a.title("my first window")
a.geometry("500x500+100+100")
m1=Menu()
l1=Menu()
l1.add_command(label="NewFile")
l1.add_command(label="OpenFile")
l1.add_command(label="SaveFile")
l1.add_command(label="save AS")
l1.add_command(label="New window")
l1.add_command(label="page setup")
l1.add_command(label="print")
l1.add_command(label="exit")
l2=Menu()
l2.add_command(label="Copy")
l2.add_command(label="Paste")
l2.add_command(label="Undo")
l2.add_command(label="delete")
l2.add_command(label="find")
l2.add_command(label="find next")
l2.add_command(label="find previous")
l2.add_command(label="Replace")
l2.add_command(label="Select all")
l2.add_command(label="time ")
l2.add_command(label="date")
l2.add_command(label="search with bring")
l3=Menu()
l3.add_command(label="Wordwrap")
l3.add_command(label="Font")
l4=Menu()
l4.add_command(label="Zoom")
l4.add_command(label="Statusbar")
l5=Menu()
l5.add_command(label="Viewhelp")
l5.add_command(label="Feedback")
l5.add_command(label="About notpad")
m1.add_cascade(label="File",menu=l1)
m1.add_cascade(label="Edit",menu=l2)
m1.add_cascade(label="Format",menu=l3)
m1.add_cascade(label="View",menu=l4)
m1.add_cascade(label="Help",menu=l5)
a.config(menu=m1)
a.mainloop()