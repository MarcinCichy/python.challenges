# Challenge: Pick Apart Your User's Input
# from RealPython, Python Basics, chapter 4.5
#

prompt = "Tell me your password: "                                                    # set variable for prompt string
password = input(prompt)                                                              # take data from user and assign it to variable password
first_letter = password [0]                                                                 # take first letter from user input 
print("The first letter you entered was: " + first_letter.upper())    # print that first letter as upper case
