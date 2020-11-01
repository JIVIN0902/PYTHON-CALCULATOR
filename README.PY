from tkinter import *

root = Tk()
root.title('Simple calculator')

e = Entry(root,width = 35,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 3,padx = 10,pady = 10)

def button_click(number):
	current = e.get()
	e.delete(0,END)

	e.insert(0, current + str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first = e.get()
	global f_num
	global math
	math = 'addition'

	f_num = int(first)
	e.delete(0,END)

def button_equal():
	second = e.get()
	e.delete(0,END)

	if math == 'addition':
		e.insert(0,f_num + int(second))

	if math == 'subtraction':
		e.insert(0,f_num - int(second))
	if math == 'multiplication':
		e.insert(0,f_num * int(second))
	if math == 'division':
		e.insert(0,(f_num )// (int(second)))
	if math == 'power':
		e.insert(0,(f_num) ** (int(second)))



def button_subtract():
	first = e.get()
	global f_num
	global math
	math = 'subtraction'

	f_num = int(first)
	e.delete(0,END)

def button_multiply():
	first = e.get()
	global f_num
	global math
	math = 'multiplication'

	f_num = int(first)
	e.delete(0,END)

def button_divide():
	first = e.get()
	global f_num
	global math
	math = 'division'

	f_num = int(first)
	e.delete(0,END)

def button_power():
	first = e.get()
	global f_num
	global math
	math = 'power'

	f_num = int(first)
	e.delete(0,END)


#define buttons
b1 = Button(root,text = '1',padx = 40,pady = 20,command =lambda:button_click(1))
b2 = Button(root,text = '2',padx = 40,pady = 20,command = lambda: button_click(2))
b3 = Button(root,text = '3',padx = 40,pady = 20,command = lambda: button_click(3))
b4 = Button(root,text = '4',padx = 40,pady = 20,command = lambda: button_click(4))
b5 = Button(root,text = '5',padx = 40,pady = 20,command = lambda: button_click(5))
b6 = Button(root,text = '6',padx = 40,pady = 20,command = lambda: button_click(6))
b7 = Button(root,text = '7',padx = 40,pady = 20,command = lambda: button_click(7))
b8 = Button(root,text = '8',padx = 40,pady = 20,command = lambda: button_click(8))
b9 = Button(root,text = '9',padx = 40,pady = 20,command = lambda: button_click(9))
b0 = Button(root,text = '0',padx = 40,pady = 20,command = lambda: button_click(0))

b_add = Button(root,text = '+',padx = 39,pady = 20,command = button_add)
b_equal = Button(root,text = '=',padx = 87,pady = 20,command = button_equal)
b_clear = Button(root,text = 'Clear',padx = 78,pady = 20,command = button_clear)
b_subtract = Button(root,text = '-',padx = 40,pady = 20,command = button_subtract)
b_multiply = Button(root,text = '*',padx = 39,pady = 20,command = button_multiply)
b_divide = Button(root,text = '/',padx = 39,pady = 20,command = button_divide)
b_power = Button(root,text = '^',padx = 38,pady = 20,command = button_power)


#put the buttons on screen


b1.grid(row = 3,column = 0)
b2.grid(row = 3,column = 1)
b3.grid(row = 3,column =2 )

b4.grid(row = 2,column = 0)
b5.grid(row = 2,column = 1)
b6.grid(row = 2,column =2)

b7.grid(row = 1,column = 0)
b8.grid(row = 1,column = 1)
b9.grid(row = 1,column = 2)

b0.grid(row = 4,column = 0)

b_add.grid(row = 5,column = 0)
b_subtract.grid(row = 6,column =0 )
b_multiply.grid(row = 6,column = 1)
b_divide.grid(row = 6,column = 2)

b_power.grid(row = 7,column = 0)

b_equal.grid(row = 5,column = 1,columnspan = 2)
b_clear.grid(row = 4,column = 1,columnspan = 2)



root.mainloop()
