#!/usr/bin/python3
"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking
"""


def isSafe(aqueen, nqueen):
    """ determines if the queens can or can't kill each other """

    for i in range(nqueen):

        if aqueen[i] == aqueen[nqueen]:
            return False

        if abs(aqueen[i] - aqueen[nqueen]) == abs(i - nqueen):
            return False

    return True


def print_result(aqueen, nqueen):
    """ prints the list with the Queens position """

    result = []

    for i in range(nqueen):
        result.append([i, aqueen[i]])

    print(result)


def Queen(aqueen, nqueen):
    """ Recursive function that executes the Backtracking algorithm"""

    if nqueen is len(aqueen):
        print_result(aqueen, nqueen)
        return

    aqueen[nqueen] = -1

    while aqueen[nqueen] < len(aqueen) - 1:

        aqueen[nqueen] += 1

        if isSafe(aqueen, nqueen) is True:

            if nqueen is not len(aqueen):
                Queen(aqueen, nqueen + 1)


def solveNQueen(size):
    """ Function that invokes the Backtracking algorithm """

    aqueen = [-1 for i in range(size)]

    Queen(aqueen, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueen(size)

