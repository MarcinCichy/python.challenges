# Challenge: Cats with Hats
# from RealPython, Python Basics, chapter 9.9
#
# You have 100 cats. One day you decide to arrange all your cats in a giant circle. 
# Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
# Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

#     The first round, you stop at every cat, placing a hat on each one.
#     The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
#     The third round, you only stop at every third cat(#3,#6,#9,#12, etc.).
#     You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).

# Write a program that simply outputs which cats have hats at the end.


cats_with_hats= []                                          # An empty list with the number of a cat in a hat
for i in range(1,101):                                      # You walk around the circle a hundred times
    for j in range(i,101,i):                                # The first round you stop at every cat, the second , you stop only at every second, etc...
        if j not in cats_with_hats:                         # Each time you stop at a cat, you check if it has a hat on
            cats_with_hats.append(j)                        # If it doesn't, then you put a hat on it
        else:                           
            cats_with_hats.remove(j)                        # If it does, then you take the hat off.
cats_with_hats.sort()                                       # Sort the list of cats in the hats
print(f"The number of cats in the hats: {cats_with_hats}")  # and show it.
