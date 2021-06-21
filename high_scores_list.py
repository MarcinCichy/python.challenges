# Challenge: Create a High Scores List
# from RealPython, Python Basics, chapter 12.7
#

import csv
from pathlib import Path


file_path = Path.home() / "practice_files" / "scores.csv"                               # sets path to "scores.csv" file
# print(file_path.exists())                                                             # check myself

with file_path.open(mode="r", encoding = "utf-8") as file:                              # open the file to read
    reader = csv.DictReader(file)                                                       # creates DictReader object
    
    temp_dict = {}                                                                      # creates empty, temporary dictionary
    for row in reader:                                                                  # in loop read content of DictReader object
        if row["name"] not in temp_dict:                                                # checks if the csv.DictReader dictionary key is in the "temp_dict" dictionary
            temp_dict[row["name"]] = row["score"]                                       # if not, it puts it in the dictionary with the corresponding value, scores
        elif int(temp_dict[row["name"]]) < int(row["score"]):                           # if the key is in the dictionary, then checks that the value assigned to the key is less than the value assigned to the row
             temp_dict[row["name"]] = row["score"]                                      # if so, it changes the value to the value in the row
       #  print (high_scores)                                                           # check myself
    #print(temp_dict)                                                                    # check myself


high_scores_file_path  = Path.home() /  "practice_files" / "high_scores.csv"            # sets path to the new"high_scores.csv" file
high_scores_file = high_scores_file_path.open(mode="w", encoding = "utf-8", newline="") # open the file to write
writer = csv.DictWriter(high_scores_file, fieldnames = ["name", "high_score"])          # uses csv.DictWriter to
writer.writeheader()                                                                    # write headers
high_scores = {}                                                                        # creates empty dictionary
for keys in temp_dict:                                                                  # for each key in temp_dict 
    high_scores["name"] = keys                                                          # places this key as the value of the "name" key and 
    high_scores["high_score"] = temp_dict[keys]                                         # adds the value of this key as the value of the high_score key, respectively                                        
    #print(high_scores)                                                                  # check myself
    writer.writerow(high_scores)                                                        # writes every rows into file