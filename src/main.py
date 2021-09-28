import urllib.request
import urllib.parse
import re
import os
from better_profanity import profanity

# Function to get profanities from the file
def getProfanities(fileName):
    print(os.path.dirname(__file__) + fileName)
    fileObj = open(os.path.dirname(__file__) + fileName, "r", encoding='utf-8')  # opens the file in read mode
    words = fileObj.read().replace(",", "\n")  # get list and prepare it for the splitlines
    profanities = words.splitlines()  # convert each line (profanity) into list element
    fileObj.close()
    for i, s in enumerate(profanities): # clean spaces from beginning and end of the words
        profanities[i] = profanities[i].strip()
    return profanities

# Censors profanities using better_profanity functions, which work except when there is @, $, *, ", '
def removeProfanities(text, profanities):
    profanity.load_censor_words(profanities)
    textCorrected = profanity.censor(text)
    return textCorrected

profanities = getProfanities("\\..\\files\\bannedWords.txt")

#Get text from file
file2correctPath = "\\..\\files\\exemple1.html"
file2correct = open(os.path.dirname(__file__) + file2correctPath, "r", encoding='utf-8')
text = file2correct.read()  # get the full html file
file2correct.close()

#Censor the profanities
text = removeProfanities(text,profanities)

#Save the changes in a new file
f = open(os.path.dirname(__file__) + "\\..\\files\\example1corrected.html", "w")
f.write(text)
f.close()

