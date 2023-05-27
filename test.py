

from tkinter import *

root = Tk()

root.geometry("500x600")
root.title("Ho")

Fullname = StringVar()
Email = StringVar()
var = IntVar()
var1 = IntVar()
var2 = IntVar()




lbl = Label(root, text="Registration Form", width=20, font=("bold", 20))
lbl.place(x=90, y=53)

lblname = Label(root, text="Name", width=10, font=("bold", 20))
lblname.place(x=30, y=130)

nameentry = Entry(root, textvar=Fullname)
nameentry.place(x=160, y=130)

lblEmail = Label(root, text="Email", width=10, font=("bold", 20))
lblEmail.place(x=30, y=200)

emailentry = Entry(root, textvar=Email)
emailentry.place(x=160, y=200)

list1 = ["", "Philippines", "Japan", "Korea", "India"]




Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=135, y=260)
Radiobutton(root, text="FeMale", padx=5, variable=var, value=2).place(x=235, y=260)


droplist = OptionMenu(root, *list1)
droplist.config(width=15)
# c.set('Select Your Country')
droplist.place(x=180, y=300)

Checkbutton(root, text="Java", variable=var1).place(x=220, y=360)
Checkbutton(root, text="Java", variable=var2).place(x=250, y=360)



root.mainloop()
