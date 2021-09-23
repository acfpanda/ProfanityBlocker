import urllib.request
import urllib.parse
import re
import os
from better_profanity import profanity

# Function to get profanities from the file
def getProfanities(fileName):
    print(os.path.dirname(__file__) + fileName)
    fileObj = open(os.path.dirname(__file__) + fileName, "r")  # opens the file in read mode
    words = fileObj.read().replace(",", "\n")  # get list and prepare it for the splitlines
    profanities = words.splitlines()  # convert each line (profanity) into list element
    fileObj.close()
    for i, s in enumerate(profanities): # clean spaces from beginning and end of the words
        profanities[i] = profanities[i].strip()
    return profanities

# Censors profanities from a text string one by one, but ignores if profanity is inside word
def removeProfanitiesV1(text):
    for i, s in enumerate(profanities):
        n = len(profanities[i])
        replace = " "
        replace += n * '*' + " "
        text = text.replace(profanities[i], replace)

    return text

# Censors profanities using better_profanity functions, which work except when there is @, $, *, ", '
def removeProfanitiesV2(text, profanities):
    profanity.load_censor_words(profanities)
    textCorrected = profanity.censor(text)
    return textCorrected

profanities = getProfanities("\\..\\files\\bannedWords.txt")

#Get text from file
file2correctPath = "\\..\\files\\example2.html"
file2correct = open(os.path.dirname(__file__) + file2correctPath, "r")
text = file2correct.read()  # get the full html file
file2correct.close()

#Censor the profanities
text = removeProfanitiesV2(text,profanities)

#Save the changes in a new file
f = open(os.path.dirname(__file__) + "\\..\\files\\example2corrected.html", "w")
f.write(text)
f.close()

#Solution: modify better_profanity to adjust the few mistakes it makes

