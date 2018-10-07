'''
Author: Diego Garcia Medina
Date: October 2018
Email: diego.garcia.medina@outlook.com
GitHub website: https://github.com/DGarciaMedina

This is a program that has the main algorithm to solve an easy/medium sudoku
game. It will display the solution and will also return the number of 
iterations that were required to solve the puzzle.

NOTE: This is the program used by Sudoku_Solver_with_GUI.py so don´t delete it
      or move it somewhere else!
'''

import numpy as np

square = [0] * 9

square[0] = list([[0], [7], [0], [2], [5], [0], [4], [0], [0]])
square[1] = list([[8], [0], [0], [0], [0], [0], [9], [0], [3]])
square[2] = list([[0], [0], [0], [0], [0], [3], [0], [7], [0]])
square[3] = list([[7], [0], [0], [0], [0], [4], [0], [2], [0]])
square[4] = list([[1], [0], [0], [0], [0], [0], [0], [0], [7]])
square[5] = list([[0], [4], [0], [5], [0], [0], [0], [0], [8]])
square[6] = list([[0], [9], [0], [6], [0], [0], [0], [0], [0]])
square[7] = list([[4], [0], [1], [0], [0], [0], [0], [0], [5]])
square[8] = list([[0], [0], [7], [0], [8], [2], [0], [3], [0]])


def check_row(square, row):
    NumList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    numbers = square[row][:]
    numbers_used = []

    for i in range(9):
        if (NumList[i] in numbers) and (i < 8) and (NumList[i] not in numbers_used):
            numbers_used.append(NumList[i])
            pass
        elif (NumList[i] in numbers) and (i == 8) and (NumList[i] not in numbers_used):
            return True
        else:
            return False


def check_column(square, column):
    NumList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    numbers = square[:][column]
    numbers_used = []

    for i in range(9):
        if (NumList[i] in numbers) and (i < 8) and (NumList[i] not in numbers_used):
            numbers_used.append(NumList[i])
            pass
        elif (NumList[i] in numbers) and (i == 8) and (NumList[i] not in numbers_used):
            return True
        else:
            return False


def check_all_rows(square):
    RowsOk = True

    for i in range(9):
        A = check_row(square, i)
        if A == False:
            RowsOk = False

    return RowsOk


def check_all_columns(square):
    ColumnsOk = True

    for i in range(9):
        A = check_column(square, i)
        if A == False:
            ColumnsOk = False

    return ColumnsOk


def set_possible_outcomes(square):
    for i in range(9):
        for j in range(9):
            if square[i][j] == [0]:
                square[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    return square


def solver(square):
    square2 = set_possible_outcomes(square)

    Solved = False
    counter = 0

    while counter < 50 and (Solved == False):
        counter += 1

        for repetition1 in range(50):
            for i in range(3):
                for j in range(3):
                    NumbersSubsquare = []
                    for k in range(i * 3, (i * 3) + 3):
                        for m in range(j * 3, (j * 3) + 3):
                            if type(square2[k][m]) == int:
                                NumbersSubsquare.append(square2[k][m])

                    for k in range(i * 3, i * 3 + 3):
                        for m in range(j * 3, j * 3 + 3):
                            if type(square2[k][m]) == list:
                                for possibility in square2[k][m]:
                                    if possibility in NumbersSubsquare:
                                        square2[k][m].remove(possibility)
                            if type(square2[k][m]) == list:
                                if len(square2[k][m]) == 1:
                                    for a in square2[k][m]:
                                        square2[k][m] = a

            for i in range(9):
                NumbersRow = []

                for j in range(9):

                    if type(square2[i][j]) == int:
                        NumbersRow.append(square2[i][j])

                for j in range(9):
                    if type(square2[i][j]) == list:
                        if len(square2[i][j]) > 1:
                            for possibility in square2[i][j]:
                                if possibility in NumbersRow:
                                    square2[i][j].remove(possibility)

                    if type(square2[i][j]) == list:
                        if len(square2[i][j]) == 1:
                            for a in square2[i][j]:
                                square2[i][j] = a

            for j in range(9):
                NumbersColumn = []

                for i in range(9):

                    if type(square2[i][j]) == int:
                        NumbersColumn.append(square2[i][j])

                for i in range(9):
                    if type(square2[i][j]) == list:
                        if len(square2[i][j]) > 1:
                            for possibility in square2[i][j]:
                                if possibility in NumbersColumn:
                                    square2[i][j].remove(possibility)
                    if type(square2[i][j]) == list:
                        if len(square2[i][j]) == 1:
                            for a in square2[i][j]:
                                square2[i][j] = a

        # for p in range(10):
        #     for i in range(9):
        #         for j in range(9):
        #
        #             if counter < 5:
        #                 for k in square2:
        #                     print(k)
        #
        #             print("\n", square2[i], "\n", i, j, counter)
        #
        #             if type(square2[i][j]) == list:
        #                 for r in range(len(square2[i][j])):
        #
        #                     print(r)
        #                     # print(square2[i],"*\n",r)
        #                     # print(square2[i][j],"**\n",r,type(square2[i][j]))
        #                     if type(square2[i][j]) == list:
        #                         square2 = check_squares2(square2, i, j, r)
        #                     print(square2, "*\n", r)
        #                     # print(square2[i][j], "**\n", r, type(square2[i][j]))


        if (check_all_columns(square2) == True) and (check_all_rows(square2) == True):
            Solved = True
            break

    return square2, counter


def check_squares2(square2, i, j, r):
    # print(square2)

    if type(square2[i][j]) == list:

        if i < 3 and j < 3:

            for k in range(0, 3):
                for m in range(0, 3):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2

            square2[i][j] = square2[i][j][r]
            return square2

        elif i >= 3 and i < 6 and j < 3:

            for k in range(3, 6):
                for m in range(0, 3):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2

            square2[i][j] = square2[i][j][r]
            return square2

        elif i >= 6 and j < 3:

            for k in range(6, 9):
                for m in range(0, 3):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2

            square2[i][j] = square2[i][j][r]
            return square2

        elif i < 3 and j < 6 and j >= 3:

            for k in range(0, 3):
                for m in range(3, 6):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2

            square2[i][j] = square2[i][j][r]
            return square2


        elif i >= 3 and i < 6 and j >= 3 and j < 6:

            for k in range(3, 6):
                for m in range(3, 6):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2

            square2[i][j] = square2[i][j][r]
            return square2

        elif i > 6 and j >= 3 and j < 6:

            for k in range(6, 9):
                for m in range(3, 6):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2

            square2[i][j] = square2[i][j][r]
            return square2

        elif i < 3 and j >= 6:

            for k in range(0, 3):
                for m in range(6, 9):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2

            square2[i][j] = square2[i][j][r]
            return square2

        elif i >= 3 and i < 6 and j >= 6:

            for k in range(3, 6):
                for m in range(6, 9):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2
            # print("\n hey")
            square2[i][j] = square2[i][j][r]
            return square2

        elif i >= 6 and j >= 6:

            for k in range(6, 9):
                for m in range(6, 9):

                    if type(square2[k][m]) == list:
                        if i == k and j == m:
                            pass
                        else:
                            for possibility in square2[k][m]:
                                # print(square2[i][j][r], possibility, square2[i][j][r] == possibility)
                                if square2[i][j][r] == possibility:
                                    return square2

            square2[i][j] = square2[i][j][r]
            return square2
    else:
        return square2


def columns2(square2, i, r):
    pass


A, B = solver(square)

for i in A:
    print(i)

print("There were", B, "iterations required.")

# A=[1,2,3,4,5]
# print(A[0])