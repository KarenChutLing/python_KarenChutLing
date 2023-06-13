#Karen Chut Ling
#20DDT21F1009

import tkinter
from tkinter import*

Automatic_Username = tkinter.Tk ()
Automatic_Username.title('Automatic Username')
Automatic_Username.minsize(height=300, width= 500)


def combine ():
    firstname.insert()
    scndname.insert()
    result = firstname and scndname
    thirdEntry.insert(result,INSERT)

def clear ():
    firstname.delete(0,END)
    scndname.delete(0,END)
    thirdEntry.delete(0,END)

def exit ():
   Automatic_Username.quit()

auto = tkinter.LabelFrame (text="Username Suggestion" , font=("Arial",12),foreground='black')
auto.grid (column=0,row=0,padx= 100 , pady=100)

firstLabel = tkinter.Label (auto, text='First Name :', font=('Arial', 12))
firstLabel.grid (column=0 , row=0)

scndLabel = tkinter.Label (auto , text="Second Name : " , font=("Arial" , 12))
scndLabel.grid (column= 0 , row= 1)

thirdLabel = tkinter.Label (auto , text="Suggested  : " , font=("Arial" , 12))
thirdLabel.grid (column= 0 , row= 2)

firstname = tkinter.Entry (auto,bd=5)
firstname.grid (column=1 , row=0)

scndname = tkinter.Entry (auto,bd=5)
scndname.grid (column=1 , row=1)

thirdEntry = tkinter.Entry (auto,bd=5)
thirdEntry.grid (column=1 , row=2)

btnCombine = tkinter.Button (auto , text='Combine', width=7 , height=1 , font=('Arial', 12) , command=combine)
btnCombine.grid (column=1 , row=3)

btnClear = tkinter.Button(auto, text = 'Clear ', width=5,height=1 , font=('Arial', 12), command=clear)
btnClear.grid (column=2 , row=3)

btnExit = tkinter.Button(text = 'Exit', width=5 , height=1 , font= ('Arial', 12 ), command=exit)
btnExit.place(x=355,y=250)

Automatic_Username.mainloop()



