'''
Author: Diego Garcia Medina
Date: October 2018
Email: diego.garcia.medina@outlook.com
GitHub website: https://github.com/DGarciaMedina

This is a program that will output a GUI with the Tkinter library where the
user is shown an empty Sudoku grid, and the initial numbers may be input
and then the program will solve it for you!

NOTE: This program requires Sudoku_Solver_algorithm.py so don´t delete it
      or move it somewhere else!
'''

from tkinter import *
import tkinter.messagebox
from Sudoku_Solver_example import solver

root = Tk()
root.geometry("1000x850+300+0")
root.title("Sudoku Solver")
root.tk.call('tk', 'scaling', 2.0)


# =====================Functions==========================

def Solve():
    for i in range(9):
        for j in range(9):
            eval("btn" + str(i) + str(j) + ".configure(fg='black')")

    square = [0] * 9

    for i in range(9):
        for j in range(9):

            if eval("btn" + str(i) + str(j) + ".get()") == "" or eval("btn" + str(i) + str(j) + ".get()").isdigit():
                if len(eval("btn" + str(i) + str(j) + ".get()")) == 0:
                    eval("btn" + str(i) + str(j) + ".delete(0,'end')")
                    eval("btn" + str(i) + str(j) + ".insert(0,'0')")
            else:
                reset()
                tkinter.messagebox.showerror("Submission Error",
                                             "Please, only input integer numbers. The characters A-Z,.-?!/#@ are not allowed.")
                return

    square[0] = list(
        [[int(btn00.get())], [int(btn10.get())], [int(btn20.get())], [int(btn30.get())], [int(btn40.get())],
         [int(btn50.get())], [int(btn60.get())], [int(btn70.get())], [int(btn80.get())]])
    square[1] = list(
        [[int(btn01.get())], [int(btn11.get())], [int(btn21.get())], [int(btn31.get())], [int(btn41.get())],
         [int(btn51.get())], [int(btn61.get())], [int(btn71.get())], [int(btn81.get())]])
    square[2] = list(
        [[int(btn02.get())], [int(btn12.get())], [int(btn22.get())], [int(btn32.get())], [int(btn42.get())],
         [int(btn52.get())], [int(btn62.get())], [int(btn72.get())], [int(btn82.get())]])
    square[3] = list(
        [[int(btn03.get())], [int(btn13.get())], [int(btn23.get())], [int(btn33.get())], [int(btn43.get())],
         [int(btn53.get())], [int(btn63.get())], [int(btn73.get())], [int(btn83.get())]])
    square[4] = list(
        [[int(btn04.get())], [int(btn14.get())], [int(btn24.get())], [int(btn34.get())], [int(btn44.get())],
         [int(btn54.get())], [int(btn64.get())], [int(btn74.get())], [int(btn84.get())]])
    square[5] = list(
        [[int(btn05.get())], [int(btn15.get())], [int(btn25.get())], [int(btn35.get())], [int(btn45.get())],
         [int(btn55.get())], [int(btn65.get())], [int(btn75.get())], [int(btn85.get())]])
    square[6] = list(
        [[int(btn06.get())], [int(btn16.get())], [int(btn26.get())], [int(btn36.get())], [int(btn46.get())],
         [int(btn56.get())], [int(btn66.get())], [int(btn76.get())], [int(btn86.get())]])
    square[7] = list(
        [[int(btn07.get())], [int(btn17.get())], [int(btn27.get())], [int(btn37.get())], [int(btn47.get())],
         [int(btn57.get())], [int(btn67.get())], [int(btn77.get())], [int(btn87.get())]])
    square[8] = list(
        [[int(btn08.get())], [int(btn18.get())], [int(btn28.get())], [int(btn38.get())], [int(btn48.get())],
         [int(btn58.get())], [int(btn68.get())], [int(btn78.get())], [int(btn88.get())]])

    A, B = solver(square)

    Found = False

    for i in range(9):
        for j in range(9):
            if eval("btn" + str(i) + str(j) + ".get()") == str(0):
                eval("btn" + str(i) + str(j) + ".configure(fg='red')")
                eval("btn" + str(i) + str(j) + ".delete(0,'end')")
                eval("btn" + str(i) + str(j) + ".insert(0,'" + str(A[j][i]) + "')")

    for i in range(9):
        for j in range(9):
            if len(eval("btn" + str(i) + str(j) + ".get()")) > 1:
                delete_arrays()

                tkinter.messagebox.showerror("Submission Error",
                                             "The Sudoku could not be solved because of the following reasons:\n\n"
                                             "     1) The grid is empty\n     2) The sudoku is too complex\n\n"
                                             "Please, try by inserting new values.")

                return


def reset():
    for i in range(9):
        for j in range(9):
            eval("btn" + str(i) + str(j) + ".delete(0,'end')")
            eval("btn" + str(i) + str(j) + ".configure(fg='black')")


def delete_arrays():
    for i in range(9):
        for j in range(9):
            if len(eval("btn" + str(i) + str(j) + ".get()")) > 1:
                eval("btn" + str(i) + str(j) + ".delete(0,'end')")


# ====================Widgets==============================

Top = Frame(root, width=800, height=75, relief=SUNKEN, bg="white")
Top.pack(side=TOP, fill=X)

BottomFrame = Frame(root, width=800, height=425, relief=SUNKEN, bg="white")
BottomFrame.pack(side=TOP, fill=X, ipady=2)

BottomSudoku = Frame(BottomFrame, width=400, height=200, relief=SUNKEN, bg="white", bd=10)
BottomSudoku.pack(side=TOP, fill=Y, padx=2, pady=2)

BottomInfo = Frame(BottomFrame, width=400, height=200, relief=FLAT, bg="white", bd=2)
BottomInfo.pack(side=TOP, fill=Y, padx=2, pady=2)

lblInfo = Label(Top, font=("Kozuka Gothic Pro EL", 50, "bold"), text="Sudoku Solver", fg="dark blue", bg="white", bd=10,
                anchor="w")
lblInfo.pack()

Name = Label(Top, font=("Kozuka Gothic Pro EL", 8, "bold"), text="Diego García Medina © 2017", fg="black", bg="white",
             bd=10, anchor="w")
Name.pack()

Instructions = Label(BottomInfo, font=("Kozuka Gothic Pro EL", 12),
                     text="\nPlease input the given numbers\n in the grid above and press the\n 'Solve' button to complete it.\n",
                     bg="white", fg="black")
Instructions.pack(side=TOP)

SubmitButton = Button(BottomFrame, text="Solve", justify="center", font=("Kozuka Gothic Pro EL", 20, "bold"),
                      command=Solve, padx=100, cursor="arrow", highlightthickness=5)
SubmitButton.pack(side=RIGHT)

ResetButton = Button(BottomFrame, text="Reset", fg="gray40", justify="center",
                     font=("Kozuka Gothic Pro EL", 20, "bold"),
                     command=reset, padx=100, cursor="arrow")
ResetButton.pack(side=LEFT)

for j in range(9):
    for i in range(9):
        exec("btn" + str(i) + str(j) + "=Entry(BottomSudoku, font=('calibri', 12, 'bold'), justify='center', width=3)")
        eval("btn" + str(i) + str(j) + ".grid(row=" + str(i) + ", column=" + str(j) + ")")


root.mainloop()
