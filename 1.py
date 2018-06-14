#Answer 1
from tkinter import *


root=Tk()

def add():
    
    dict={}
    key=keyE.get()
    value=valueE.get()
    dict[key]=value
    
    for i in dict:
        listbox.insert(END,i)
        keyE.delete(0,'end')
        valueE.delete(0,'end')
        keyE.focus()

lbl1=Label(root,text="Enter Name:")
lbl1.grid(row=1,column=0)

lbl2=Label(root,text="Enter Mobile Number:")
lbl2.grid(row=2,column=0)

keyE=Entry(root)
keyE.grid(row=1,column=1)

valueE=Entry(root)
valueE.grid(row=2,column=1)

addB=Button(root,text='ADD',command=add)
addB.grid(row=3,column=1)

listbox=Listbox(root,height=8,width=40)
listbox.grid(row=4,column=0,rowspan=10,columnspan=2)

sb=Scrollbar(root)
sb.grid(row=4,column=1,sticky='e')

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

root.mainloop()
