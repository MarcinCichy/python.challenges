# Challenge: Wax Poetic
# from RealPython, Python Basics, chapter 9.5
#

import random

# The list of poem ingridients.
poem_ingridients = [
                ["fossil", "horse", "aadvark", "judge", "chef", "mango", "extrovert", "gorilla"],                # nouns; required number of words = 3
                ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"],                       # verbs; required number of words = 3
                ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"],                      # adjectives; required number of words = 3
                ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"],          # prepositions; required number of words = 2
                ["curiousl", "extravagantly", "tantalizingly", "furiously", "sensuously"],                       # adverbs; required number of words = 1
 ] 


def drawn_words (words_list):
    """ The function randomly selects words from the list. 
        Depending on the part of the sentence (nouns, verbs, adjectives, prepositions, adverbs), 
        it selects the required number of words and returns it in one list. """

    words = []
    for i in range (0,len(words_list)):
        if words_list.index(words_list[i]) < 3:         # lists from 0 to 2 (nouns, verbs, adjectives) needs 3 words
            for j in range (0,3):
                word = random.choice(words_list[i])
                words.append(word)
        elif words_list.index(words_list[i]) == 3:      # list 3 (prepositions) need 2 words
            for j in range (0,2):
                word = random.choice(words_list[i])
                words.append(word)
        else:                                           
            for j in range (0,1):                       # list 4 (adverbs) need 1 word
                word = random.choice(words_list[i])
                words.append(word)
    return words

new_list = drawn_words(poem_ingridients)

## Little help to write poem, what index is what part of sentence ;)    
# noun1 - new_list[0]
# noun2 - new_list[1]
# noun3 - new_list[2]
# verb1 - new_list[3]
# verb2 - new_list[4]
# verb3 - new_list[5]
# adj1 - new_list[6]
# adj2 - new_list[7]
# adj3 - new_list[8]
# prep1 - new_list[9]
# prep2 - new_list[10]
# adverb1 - new_list[11]


# indefinite article - which one to use
if new_list[6][0] == "i" or new_list[6][0] == "e":
    start_letter = "An"
else:
    start_letter = "A"


# write a poem :))))
print(f"""
        {start_letter} {new_list[6]} {new_list[0]}

        {start_letter} {new_list[6]} {new_list[0]} {new_list[3]} {new_list[9]} the {new_list[7]} {new_list[1]}
        {new_list[11]}, the {new_list[0]} {new_list[4]}
        the {new_list[1]} {new_list[5]} {new_list[10]} a {new_list[8]} {new_list[2]}

                                                                    Your Computer
                                                                    Inspired by Clifford Pickover
    """)


