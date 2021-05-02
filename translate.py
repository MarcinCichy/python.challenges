# Challenge: Turn Your User Into a L33t H4xor
# from RealPython, Python Basics, chapter 4.9
#
 
prompt = "Enter some text: "                                                    # set variable for prompt string
user_phrase = input (prompt)                                             # take data from user and assign it to variable user_phrase

# replace letters: a, b, e, i, o, s, t by digits: 4, 8, 3, 1, 0, 5, 7. Used replace()method and assign new strings to variable new_user_phrase
new_user_phrase = user_phrase.replace("a", "4")             
new_user_phrase = new_user_phrase.replace("b", "8")  
new_user_phrase = new_user_phrase.replace("e", "3")
new_user_phrase = new_user_phrase.replace("l", "1")
new_user_phrase = new_user_phrase.replace("o", "0")
new_user_phrase = new_user_phrase.replace("s", "5")
new_user_phrase = new_user_phrase.replace("t", "7")
print (new_user_phrase)
