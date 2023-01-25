from tkinter import *
root = Tk()
root.title('Domik')
root.geometry('800x600')
canvas = Canvas(root, width=400, height=500, bg='gray')
canvas.pack()
def color1():
    canvas.itemconfig(oval, fill='orange')
def color2():
    canvas.itemconfig(rectangle, fill='black')
def color3():
    canvas.itemconfig(polygon, fill='yellow')
oval = canvas.create_oval(250,3,400,180, width=2,fill='pink', outline='red')
rectangle = canvas.create_rectangle(100,350,300,500, width=3,fill='yellow', activefill='brown', activeoutline='white')
polygon = canvas.create_polygon([100,350],[195,230], [300,350],)
b1 = Button(root, height=3, width=4, text='Крыша', bg='cyan', activebackground='red', command=color3)
b2 = Button(root, height=3, width=4, text='Фундамент дома', bg='red', activebackground='white', command=color2)
b3 = Button(root, height=3, width=4, text='Солнце', bg='red', activebackground='white',command=color1)
b1.pack()
b2.pack()
b3.pack()
root.mainloop()