from tkinter import * 
from tkinter import messagebox 
win= Tk() 
win.geometry('500x300') 
py='' 
ja='' 
cc='' 
py_=0 
ja_=0 
cc_=0 
#=======func===========
def run(): 
    global cc , ja , py , cc_ , ja_ , py_ 
    if i_python.get() == 1: 
        py= 'python = 250' 
        py_ = 250 
    if i_java.get() == 1: 
        ja= 'java = 200' 
        ja_=200 
    if i_c.get() == 1: 
        cc= 'c# = 170' 
        cc_=170 
    sum=py_ + ja_ + cc_ 
    messagebox.showinfo('price',f'{py} \n {ja} \n {cc} \n sum={py_ + ja_ + cc_}') 
 
i_python =IntVar() 
i_java =IntVar() 
i_c =IntVar() 
v1=IntVar(win,0)
v2=IntVar(win,0)
#===========widget================
lbl_name=Label(win,text='Name:')
lbl_name.place(x=15,y=20) 
lbl_lname=Label(win,text='Lastname:')
lbl_lname.place(x=15,y=60)
lbl_Q=Label(win,text='Choose your desired training course:')
lbl_Q.place(x=15,y=150)

ent_name=Entry(win,font='arial 9')
ent_name.place(x=100,y=22)
ent_lname=Entry(win,font='arial 9')
ent_lname.place(x=100,y=60)

rb1=Radiobutton(win,text='Female',font='arial 9',variable=v1)
rb1.place(x=15,y=100)

rb2=Radiobutton(win,text='Male',font='arial 9',variable=v2)
rb2.place(x=90,y=100)


python = Checkbutton(win, text='python',variable= i_python) 
java = Checkbutton(win, text='java',variable= i_java) 
c = Checkbutton(win, text='c#',variable= i_c) 
 
python.grid(row=0,column=0,padx=60,pady=200) 
java.grid(row=0,column=1,padx=40,pady=10) 
c.grid(row=0,column=2,padx=10,pady=10) 
 
btn_sign = Button(win,text='Sign',width=10,command=run) 
btn_sign.place(x=390,y=230)
 
 
 
 
win.mainloop()