from tkinter import *
from tkinter import filedialog



class Cunverter:
    def __init__(self,master) :
        
        master.title("Cunverter")
        master.geometry("350x200")
        master.config(bg='black')
        master.resizable(False,False)
        self.qyma=""
        self.urrnsy=""
        self.entry_value=""
        self.value
        self.omar=Entry(width=4,bg='white',font=('Arial Blod',28)).place(x=0,y=0)
        Entry(width=4,bg='white',textvariable=self.entry_value,font=('Arial Blod',28)).place(x=262,y=0)
        Entry(width=4,bg='white',textvariable=self.value,font=('Arial Blod',28)).place(x=130,y=100)
        Button(width=4,height=4,text="=",activebackground="#F5E216",relief="flat",bg="lightblue").place(x=130,y=20)#19

    def value (self,valu):
       self.entry_value*self.urrnsy.set(self.omar)
   
root=Tk()
currncy=Cunverter(root)
root.mainloop()        