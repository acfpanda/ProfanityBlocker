import urllib.request
import urllib.parse
import re
import os
from better_profanity import profanity

# Function to get profanities from the file
def getProfanities(fileName):
    fileObj = open(os.path.dirname(__file__) + fileName, "r")  # opens the file in read mode
    words = fileObj.read().replace(",", "\n")  # get list and prepare it for the splitlines
    profanities = words.splitlines()  # convert each line (profanity) into list element
    fileObj.close()
    for i, s in enumerate(profanities): # clean spaces from beginning and end of the words
        profanities[i] = profanities[i].strip()
    return profanities

profanities = getProfanities("\\..\\bannedWords.txt")
profanity.load_censor_words(profanities)
print(profanity.censor('damn i have to watch a lot of fucking f u c k python tutorials these dick hole days'))

# f = open("juice.html","w")

# 1 - Get HTML text file

# 2 - Find inside <body>, normal text that has profanities
