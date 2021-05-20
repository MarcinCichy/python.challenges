# Challenge: Find the Factors of a Number
# from RealPython, Python Basics, chapter 8.4
#

number = int(input("Enter a positive integer: "))

for i in range (number +1):
    if i != 0:
        if number%i == 0:
            print (f'{i} is a factor of {number}')