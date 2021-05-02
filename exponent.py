# Challenge: Perform Calculations on User Input
# from RealPython, Python Basics, chapter 5.3
#

base = input ("Enter a base: ")             # take data from User and assign it to variable base
exponent = input ("Enter a exponen: ") # take another data from User and assign it to variable exponent
base = float(base)                               # set strin as float
exponent = float(exponent)                  #set strin as float
result = base ** exponent                        # raise base to the power of exponent
print (f"{base } to the  power of  {exponent}  =  {result}")
                  
