# Challenge: Capital City Loop
# from RealPython, Python Basics, chapter 9.7
#

import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phenix',
    'Arkansas': 'Little Rock',
    'California':'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

state, capital = random.choice(list(capitals_dict.items()))                         # assign randomly selected keys and their value to variables 'state' and 'capital'

user_answer = ""
while user_answer.lower() != capital.lower() and user_answer.lower() != 'exit':     # while loop works as long as user don't write corect name of capitol or exit
    user_answer = input(f'Write a {state} capital city: ')

if user_answer.lower() == 'exit':
    print(f'The capital of {state} is {capital}.')
    print('Goodbye')
else:
    print("Correct")



