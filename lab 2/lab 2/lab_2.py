
#gissnings tid för detta program = 20 timmar

from tkinter import *
import random

root = Tk()
root.iconbitmap('') #icon på programet
root.title("Mastermind") #titel of the program
#Buttons---------------------------------------------------------------------------------------------------------
def Click_1():
    return

def Click_2():
    return

def Click_3():
    return

def Click_4():
    return

def Click_5():
    return

def Click_6():
    return

def Click_7():
    return

def Click_8():
    return


Button_1 = Button(root, bg="red", width=3, command=Click_1)
Button_2 = Button(root, bg="blue", width=3, command=Click_2)
Button_3 = Button(root, bg="green", width=3, command=Click_3)
Button_4 = Button(root, bg="yellow", width=3, command=Click_4)
Button_5 = Button(root, bg="brown", width=3, command=Click_5)
Button_6 = Button(root, bg="orange", width=3, command=Click_6)
Button_7 = Button(root, bg="black", width=3, command=Click_7)
Button_8 = Button(root, bg="white", width=3, command=Click_8)

Button_1.grid(row=1, column=1)
Button_2.grid(row=1, column=2)
Button_3.grid(row=1, column=3)
Button_4.grid(row=1, column=4)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)
Button_7.grid(row=2, column=3)
Button_8.grid(row=2, column=4)


root.mainloop()