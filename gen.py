# Name: Password Generator 
# Author: Ghoul (@NotGhoull)
# Date: 15/02/2022
# Description: A simple password generator

from classes.generator import Generator as gen

length = input("Please enter the length of the password\n>>> ")

if length == type(int):
    print(gen.generate_pass(length))
else:
    raise ValueError("Length has to be a number!")