###
# CS 3C Advanced Data Structures and Algorithms in Python
# Lab 1: Classes and Object-Oriented Programming
# Application: Movie Class
# Solution File: carolynPyunLab1.py
# Date:  1/11/22
###

class Movie:
    """ a class used to represent the Movie and the list

            Attributes
            name : string
                name of movie
            year : int
                year of movie
            __movieList : movie
                list of movies
    """

    MAX_LEN = 50
    DEFAULT_NAME = ""
    DEFAULT_YEAR = 2021

    __movieList = []  # stores movie objects

    def __init__(self, input_name=DEFAULT_NAME, input_year=DEFAULT_YEAR):
        self.name = input_name
        self.year = input_year

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

    def setName(self, input_name):
        # Returns false if invalid input
        # Sets name of movie
        if not self.strOK(input_name):
            return False
        else:
            self.name = input_name
            return True

    def setYear(self, input_year):
        # Returns false if invalid input
        # Sets year of movie
        if not self.yearOK(input_year):
            return False
        else:
            self.year = input_year
            return True

    def add(self, movie):  # adds movie to the list, default values if invalid
        title = input("Name: ")
        year = int(input("Year: "))
        movie.setName(title)
        movie.setYear(year)
        self.__movieList.append(movie)
        print(f"{movie.getName()} was added.")

    def delete(self, index):  # deletes specific movie in list
        if index <= len(self.__movieList):
            print(f"{self.__movieList[index - 1].getName()} was deleted.")
            self.__movieList = self.__movieList[:index - 1] + self.__movieList[index:]
        else:
            print("Invalid movie number!")

    def list(self):  # Prints copy of current movie list
        if len(self.__movieList) == 0:
            print("Out of movies...order more!")
        else:
            index = 1
            for movie in self.__movieList:
                print(f"{index}. {movie.getStr()}")
                index += 1

    def getStr(self):  # Returns string w all info of single movie entry in list
        info = self.getName() + " (" + str(self.getYear()) + ")"
        return info

    def strOK(self, the_str):  # Check if valid string
        if len(the_str) <= self.MAX_LEN:
            return True
        return False

    def yearOK(self, the_year):  # Check if valid year
        if 1000 < the_year < 2022:
            return True
        return False
