###
# CS 3C Advanced Data Structures and Algorithms in Python
# Description:  This program is a driver demo for the Movie class.
# Solution File: carolynPyunLab1demo.py
# Date:  1/11/22
#

# Import the Movie class from the carolynPyunLab1 module
from carolynPyunLab1 import Movie


def main():
    command = ""
    movie = Movie()
    while command != "exit":    # Take in input until exit
        print_menu()
        command = input("Command: ").lower()
        if command == "list":
            movie.list()
        elif command == "add":
            new_movie = Movie()
            movie.add(new_movie)
        elif command == "del":
            index = int(input("Number: "))
            movie.delete(index)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid option!")
        print()


def print_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()


if __name__ == '__main__':
    main()

# Program run
'''
COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: add
Name: Monty Python and the Holy Grail
Year: 1975
Monty Python and the Holy Grail was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: On the Waterfront
Invalid option!

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: add
Name: On the Waterfront
Year: 1954
On the Waterfront was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: add
Name: Cat on a Hot Tin Roof
Year: 1958
Cat on a Hot Tin Roof was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: list
1. Monty Python and the Holy Grail (1975)
2. On the Waterfront (1954)
3. Cat on a Hot Tin Roof (1958)

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: add
Name: Breaking Point
Year: 2021
Breaking Point was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: list
1. Monty Python and the Holy Grail (1975)
2. On the Waterfront (1954)
3. Cat on a Hot Tin Roof (1958)
4. Breaking Point (2021)

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: del
Number: 2
On the Waterfront was deleted.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: list
1. Monty Python and the Holy Grail (1975)
2. Cat on a Hot Tin Roof (1958)
3. Breaking Point (2021)

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: exit
Bye!
'''