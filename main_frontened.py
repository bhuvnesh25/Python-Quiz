#Import everything from tkinter
from tkinter import *

#create Window object
window=Tk()
window.geometry("500X500")

#define labels
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

#define Entries
title=StringVar()
e1=Entry(window)
e1.grid(row=0,column=1)

author=StringVar()
e2=Entry(window)
e2.grid(row=0,column=3)

year=StringVar()
e3=Entry(window)
e3.grid(row=1,column=1)

isbn=StringVar()
e4=Entry(window)
e4.grid(row=1,column=3)

#define Listbox
list1=Listbox(window,height=10,width=40)
list1.grid(row=2,column=0,rowspan=10,columnspan=2)

#Attach Scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#define button

b1=Button(window,text="View All",width=15)
b1.grid(row=2,column=3)

b1=Button(window,text="Search",width=15)
b1.grid(row=3,column=3)

b1=Button(window,text="Add Entry",width=15)
b1.grid(row=4,column=3)

b1=Button(window,text="Update",width=15)
b1.grid(row=5,column=3)

b1=Button(window,text="Exit",width=15)
b1.grid(row=6,column=3)


window.mainloop()