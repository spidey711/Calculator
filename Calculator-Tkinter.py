# imports
try:
    from tkinter import *
except ImportError as ie:
    print(ie)

# window setup
root = Tk()
root.title("Calculator App")

# global variables
f_num = " " # number from input box
math = " " # operation (+, -, *, /)

# Input Box Display
entry = Entry(root, width=50, borderwidth=4)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Operation Functions
def buttonClick(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def buttonClear():
    entry.delete(0, END)

def buttonAdd():
    firstNumber = entry.get()
    global f_num
    global math
    f_num = int(firstNumber)
    math = "addition"
    entry.delete(0, END)

def buttonSubtract():
    firstNumber = entry.get()
    global f_num
    global math
    f_num = int(firstNumber)
    math = "subtraction"
    entry.delete(0, END)

def buttonMultiply():
    firstNumber = entry.get()
    global f_num
    global math
    f_num = int(firstNumber)
    math = "multiplication"
    entry.delete(0, END)

def buttonDivide():
    firstNumber = entry.get()
    global f_num
    global math
    f_num = int(firstNumber)
    math = "division"
    entry.delete(0, END)

def buttonExponent():
    firstNumber = entry.get()
    global f_num
    global math
    f_num = int(firstNumber)
    math = "exponent"
    entry.delete(0, END)
    
def buttonEqual():
    secondNumber = int(entry.get())
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + secondNumber)
    elif math == "subtraction":
        entry.insert(0, f_num - secondNumber)
    elif math == "multiplication":
        entry.insert(0, f_num * secondNumber)
    elif math == "division": 
        entry.insert(0, f_num / secondNumber)
    elif math == "exponent":
        entry.insert(0, f_num ** secondNumber)

    # Calculation History
    with open("calculatorHistory.txt", "a") as file:
        try:
            if math == "addition":
                file.write("{} + {} = {}\n".format(f_num, secondNumber, f_num + secondNumber))
            elif math == "subtraction":
                file.write("{} - {} = {}\n".format(f_num, secondNumber, f_num - secondNumber))
            elif math == "multiplication":
                file.write("{} x {} = {}\n".format(f_num, secondNumber, f_num * secondNumber))
            elif math == "division":
                file.write("{} / {} = {}\n".format(f_num, secondNumber, f_num / secondNumber))
            elif math == "exponent":
                file.write("{} ^ {} = {}\n".format(f_num, secondNumber, f_num ** secondNumber))
        except Exception as e:
            print(e)

# Buttons Setup
button0 = Button(root, text=0, padx=40, pady=20 ,command=lambda:buttonClick(0))
button1 = Button(root, text=1, padx=40, pady=20, command=lambda:buttonClick(1))
button2 = Button(root, text=2, padx=40, pady=20, command=lambda:buttonClick(2))
button3 = Button(root, text=3, padx=40, pady=20, command=lambda:buttonClick(3))
button4 = Button(root, text=4, padx=40, pady=20, command=lambda:buttonClick(4))
button5 = Button(root, text=5, padx=40, pady=20, command=lambda:buttonClick(5))
button6 = Button(root, text=6, padx=40, pady=20, command=lambda:buttonClick(6))
button7 = Button(root, text=7, padx=40, pady=20, command=lambda:buttonClick(7))
button8 = Button(root, text=8, padx=40, pady=20, command=lambda:buttonClick(8))
button9 = Button(root, text=9, padx=40, pady=20, command=lambda:buttonClick(9))

# Buttons setup (operations)
button_add = Button(root, text='+', padx=38, pady=20, command=buttonAdd)
button_subtract = Button(root, text='-', padx=40, pady=20, command=buttonSubtract)
button_multiply = Button(root, text='*', padx=40, pady=20, command=buttonMultiply)
button_divide = Button(root, text='/', padx=40, pady=20, command=buttonDivide)
button_equal = Button(root, text='=', padx=40, pady=20, command=buttonEqual)
button_clear = Button(root, text='clear', padx=100, pady=20, command=buttonClear)
button_exponent = Button(root, text='^', padx=40, pady=20, command=buttonExponent)

# Button arrangements
button0.grid(row=4, column=1)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

# Button arrangements (operations)
button_add.grid(row=4, column=0)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=2)
button_equal.grid(row=5, column=1)
button_clear.grid(row=6, column=0, columnspan=3)
button_exponent.grid(row=6, column=1)

# Loop to keep calculator window running
root.mainloop()
