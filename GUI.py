from tkinter import *

root = Tk()
root.title("Basic Calculator")

screen = Entry(root,width = 35)
screen.grid(row = 0, column = 0, columnspan = 3)
index = 0
results = 0
operation = ""  
#functions
def click(num):
    global index
    screen.insert(index,num)
    index += 1
def clear():
    screen.delete(0,END)
def add():
    global results
    global operation
    first_number = screen.get()
    results = float(first_number)
    operation = "+"
    screen.delete(0,END)
def sub():
    global results
    global operation
    first_number = screen.get()
    results = float(first_number)
    operation = "-"
    screen.delete(0,END)
def mul():
    global results
    global operation
    first_number = screen.get()
    results = float(first_number)
    operation = "*"
    screen.delete(0,END)
def div():
    global results
    global operation
    first_number = screen.get()
    results = float(first_number)
    operation = "/"
    screen.delete(0,END)
def result():
    global results
    global operation
    second_number = screen.get()
    screen.delete(0,END)
    if operation == "+":
        screen.insert(0,results + float(second_number))
    elif operation == "-":
        screen.insert(0,results - float(second_number))
    elif operation == "*":
        screen.insert(0,results * float(second_number))
    elif operation == "/":
        screen.insert(0,results / float(second_number))


    

#make buttons
button_9 = Button(root,text = "9", padx = 20, pady = 20, command = lambda:click(9))
button_8 = Button(root,text = "8", padx = 20, pady = 20, command = lambda:click(8))
button_7 = Button(root,text = "7", padx = 20, pady = 20, command = lambda:click(7))


button_6 = Button(root,text = "6", padx = 20, pady = 20, command = lambda:click(6))
button_5 = Button(root,text = "5", padx = 20, pady = 20, command = lambda:click(5))
button_4 = Button(root,text = "4", padx = 20, pady = 20, command = lambda:click(4))


button_3 = Button(root,text = "3", padx = 20, pady = 20, command = lambda:click(3))
button_2 = Button(root,text = "2", padx = 20, pady = 20, command = lambda:click(2))
button_1 = Button(root,text = "1", padx = 20, pady = 20, command = lambda:click(1))

button_0 = Button(root,text = "0", padx = 20, pady = 20, command = lambda:click(0))
button_add = Button(root,text = "+", padx = 20, pady = 20, command = lambda:add())
button_sub = Button(root,text = "-", padx = 20, pady = 20, command = lambda:sub())
button_div = Button(root,text = "/", padx = 20, pady = 20, command = lambda:div())
button_mul = Button(root,text = "*", padx = 20, pady = 20, command = lambda:mul())
button_clear = Button(root,text = "c", padx = 20, pady = 20, command = lambda:clear())
button_equal = Button(root,text = "=", padx = 90, pady = 20, command = lambda:result())

#render Buttons
button_9.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_7.grid(row = 1, column = 2)

button_6.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_4.grid(row = 2, column = 2)

button_3.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_1.grid(row = 3, column = 2)

button_0.grid(row = 4, column = 0)
button_add.grid(row = 4, column = 1)
button_sub.grid(row = 4, column = 2)
button_mul.grid(row = 5, column = 1)
button_div.grid(row = 5, column = 2)
button_clear.grid(row = 5, column = 0)
button_equal.grid(row = 6, column = 0,columnspan = 3)
root.mainloop()