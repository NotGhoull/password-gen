# Name: Password Generator 
# Author: Ghoul (@NotGhoull)
# Date: 15/02/2022
# Description: A simple password generator

#? Import the generator class
from classes.generator import Generator as gen

#? ask the user for the length
length = input("Please enter the length of the password\n>>> ")

#? Check whether the length is an integer
if length == type(int):
    #? If it is, generate the password
    print(gen.generate_pass(length))
else:
    #? If it is not, tell the user to enter an integer
    raise ValueError("Length has to be a number!")