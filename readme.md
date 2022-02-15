# Code

if you want to use this in your application then just import the generator class from classes.generator
(Codded in python: 3.9.5)

## Code example

### Pre-defined input

```python
#? import the generator class as gen
from classes.generator import Generator as gen

#? print out the return value of generate_pass()
print(gen.generate_pass(10))
```

### user input

```python
#? Import generator class
from classes.generator import Generator as gen

#? Ask the user for the length.
length = input("Please enter the length of the password\n>>> ")
# Forced int: length: int = input("Please enter the length of the password\n>>> ")
# If this is incorrect it will throw an exception even with a try statment


#? Check if the length is a int
if length == type(int):
    #? If it is a int then we run the function with length as the argument.
    print(gen.generate_pass(length))
else:
    #? If it's not then we raise an error. This could also be changed to a print and call a function to restart the code
    raise ValueError("Length has to be a number!")

```

---

## Functions

>### generate_password()
>returns the password in a string format
