from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("500x400+10+20")
window.title("Welcome to Python Programming")

#Button widgets
button = Button(window, text = "This is a button", fg = "Orange", bg = "Blue", bd = 5)
button.place(x = 50, y = 50)

#Label widget
label = Label(window, text = "This is a label", fg = "Red", bg = "White")
label.place(x=60, y = 30)

#Text field
text = Entry(window, font = ("Times New Roman", 12), bd = 5)
text.place(x = 15, y = 80)

#Radio button
radio1 = Radiobutton(window, text = "Male", value = 1 )
radio2 = Radiobutton(window, text ="Female", value = 2)
radio1.place(x = 15, y = 100)
radio2.place(x = 70, y = 100)

#List box
var = IntVar()
var.set("Student1")
data = "Student1"
data1 = "Student2"
data2 = "Student3"
listbox = Listbox(window, selectmode = 'multiple', height = 5, width = 20)
listbox.insert(END, data)
listbox.insert(END, data1)
listbox.insert(END, data2)
listbox.place(x = 15, y = 130)

#Combo box
alldata = data, data1, data2
combobox = ttk.Combobox(window, values = alldata)
combobox.place(x = 15, y = 220)

window.mainloop()
