from turtle import *
from tkinter import *
ch=3
n=12
m=3
d=1
lenn=360/n*m
def hexcollor(n=0):
    c=str(hex(n%16777216))[2:]
    return '#'+'0'*(6-len(c))+c
def drow(n,lenn):
    for i in range(n):
        forward(lenn)
        right((180-((n-2)*180)/n)%360)
def drowrombs1(n,lenn):
    for i in range(n):                  
        right((180-((n-2)*180)/n)%360)
        drow(n,lenn)
def drowrombs2(n,lenn,d):
    for i in range(n//2+n%2):
        forward(lenn)
        right(d)
        for j in range(n+n%2):
            forward(lenn)
            right((180-d*i)%360)
            forward(lenn)
            right((180+d*(i+1))%360)
def choice(event):
    reset()
    try:
        n=int(entry1.get())
        m=int(entry2.get())
    except ValueError:
        print('Правильно введіть параметри малювання')
        return
    ch=First.get()
    if(ch==0):
        print("Ви не зробили вибір що намалювати")
        return
    d=360//n
    lenn=360/n*m
    color('#55aaff','#2281ff')
    speed(0)
    width(2)
    begin_fill()
    print('Малюється')
    if(ch==1):
        up()
        goto(-lenn,55*m*2)
        down()
        drow(n,lenn*2)
    elif(ch==2):
        drowrombs1(n,lenn)
    elif(ch==3):
        forward(-lenn)
        drowrombs2(n,lenn,d)
My_window=Tk()
My_window.title("Вибор малюнку")
My_window.geometry("300x300")
My_window["bg"]="#2281ff"
First=IntVar()
First1=Radiobutton(My_window,text='n Кутник',variable=First,value=1,fg='#223366',font=16,bg='#2281ff')      
First1.place(x=20,y=60)
First2=Radiobutton(My_window,text='Сітка ромбів\nметод №1    ',variable=First,value=2,fg='#223366',font=16,bg='#2281ff') 
First2.place(x=20,y=90)
First3=Radiobutton(My_window,text='Сітка ромбів\nметод №2    ',variable=First,value=3,fg='#223366',font=16,bg='#2281ff')
First3.place(x=150,y=90)
b1=Button (My_window,text='Намалювати',bg='#55aaff',fg='#223366',padx='5',pady='3',font='16')
b1.place(x=90,y=230)
label1=Label(My_window,text='Виберіть що намалювати',fg="#000000",bg="#2281ff",justify=LEFT,font=150)
label1.place(x=50,y=10)
label2=Label(My_window,text='Виберіть n',fg="#223366",bg="#2281ff",justify=LEFT,font=150)
label2.place(x=10,y=158)
label3=Label(My_window,text='Масштаб',fg="#223366",bg="#2281ff",justify=LEFT,font=150)
label3.place(x=10,y=188)
entry1=Entry(My_window, bg='#5fafff',width=3,)
entry1.place(x=105,y=160)
entry2=Entry(My_window, bg='#4499ee',width=2,)
entry2.place(x=90,y=190)
entry2.insert(0,3)
b1.bind('<Button-1>',choice)
end_fill()
My_window.mainloop()   