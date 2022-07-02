"""
open mode= options
r: read-only
w: write-only (erases everything else that is already on the file)
a: read and write

FILEPATHS

ABSOLUTE FILEPATH
every filepath that starts with a slash starts its way from the root folder of the system
example: /users/kauaj/Idea Projects/Aluno/src/Main.java

RELATIVE FILEPATH
filepaths we're already used to, related to the folder where the file is being held
example: ./images/strawberry.png

HOW TO MOVE ONE DIRECTORY UP
to get something from a folder that is above the file you're working with or even inside it, use two dots
example: ../PHPStudies/day6/trial.php


"""

with open("myfile.txt", mode="w") as file:
    file.write("Hello")

with open("C:/Users/kauaj/Downloads/Jugi.txt") as file:
    print(file.read())
