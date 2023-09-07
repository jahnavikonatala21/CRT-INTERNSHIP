import tkinter
from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self,root):
        self.root=root
        self.root.title("TO-DO APPLICATION")
        self.root.geometry('650x400+400+100')
         
        self.label1=Label(self.root,text='TO-DO-LIST',font ='bold',width=10,bd=5,bg='black',fg='white')
        self.label1.pack(side='top',fill=BOTH)
        

        self.label2=Label(self.root,text='Add Task',font ='bold',width=10,bd=5,bg='black',fg='white')
        self.label2.place(x=40,y=54)
        

        self.label3=Label(self.root,text='Tasks',font ='bold',width=10,bd=5,bg='black',fg='white')
        self.label3.place(x=320,y=54)

        self.main_text = Listbox(self.root,height=9,bd=5,width=23,font='ariel')
        self.main_text.place(x=320,y=100)

        self.text=Text(self.root,bd=5,height=2,width=23,font='ariel')
        self.text.place(x=20,y=120)
        
        def add():
            add_task=self.text.get(1.0,END)
            self.main_text.insert(END,add_task)
            with open('data.txt','a') as file:
                file.write(add_task)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)

        def delete():
            del_task = self.main_text.curselection()
            look = self.main_text.get(del_task)
            with open('data.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for  line in new_f:
                    item = str(look)                
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(del_task)
        

        with open('data.txt','r') as file:
            read=file.readlines()
            for i in read:
                ready=i.split()
                self.main_text.insert(END,ready)
            file.close()
            
        self.button=Button(self.root,text="Add",font='bold',width=10,bd=5,bg='black',fg='white',command=add)
        self.button.place(x=30,y=200)

        self.button=Button(self.root,text="Delete",font='bold',width=10,bd=5,bg='black',fg='white',command=delete)
        self.button.place(x=30,y=250)


def main():
    root=Tk()
    ui=todo(root)
    root.mainloop()
if __name__=="__main__":
    main()