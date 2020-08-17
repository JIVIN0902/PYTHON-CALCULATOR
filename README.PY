# PYTHON-CALCULATOR
PYTHON CODE FOR A SIMPLE CALCULATOR

def add(x,y):
    return x + y
    
def subtarct(x,y):
    return x - y
   
def multiply(x,y):
    return x * y

def divide(x,y):
    try:
        x//y
    except ZeroDivisionError:
        print("Can't divide by zero!")
        
def square(x):
    return x**2

def cube(x):
    return x **3
    
def recal():
    ask = input('Do you want to do another calculation?(yes or no) ')
    return ask.startswith('y')
    
    
def ask():
    f = ''
    s = ''
    
    while f.isdigit() == False or s.isdigit() == False:
        f = input('Enter first number : ')
        s = input("Enter second number  : ")
    return f , s
    
operands = ['+','-','*','/','sq','cu','%']


def operate():
    operator = ''
    while operator not in operands:
        operator = input('Enter an operator: ')
        
    return operator
    
def percent(x,y):
    return (x/100) * y
    
print('This is a simple calculator!\nFirst enter the number that you want to operate on.\nThen enter the operand(+,-,*,/,sq,cu) of your choice.\nThen enter the second number and i will print the result.\n\nIF YOU WANT TO SQUARE OR CUBE JUST PUT 0 AS SECOND NUMBER. ')


while True:
    f_num, s_num = ask()
    f_num = int(f_num)
    s_num = int(s_num)
    
    operand = operate()
    
    if operand == '+':
        print(add(f_num,s_num))
    elif operand == '-':
        print(subtract(f_num,s_num))
    elif operand == '*':
        print(multiply(f_num,s_num))
    elif operand == '/':
        print(divide(f_num,s_num))
    elif operand == 'sq':
        print(square(f_num))
    elif operand == 'cu':
        print(cube(f_num))
    elif operand == '%':
        print(percent(f_num,s_num))
        
    if not recal():
        break
    
    
