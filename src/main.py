import urllib.request
import urllib.parse
import re
import os
from better_profanity import profanity

file2correctName = "example2.html"  # HERE we specify the name of the file that must be corrected #

correctedFileName = "example2corrected.html"  # HERE we specify the name of the result file #


# Function to get profanities from the file
def getProfanities(fileName):
    try:
        fileObj = open(os.path.dirname(__file__) + fileName, "r", encoding='utf-8')  # opens the file in read mode
        words = fileObj.read().replace(",", "\n")  # get list and prepare it for the splitlines
        profanities = words.splitlines()  # convert each line (profanity) into list element
        fileObj.close()
    except FileNotFoundError:
        print("File \"bannedWords.txt\" not found in Files folder")
        exit()

    for i, s in enumerate(profanities):  # clean spaces from beginning and end of the words
        profanities[i] = profanities[i].strip()
    return profanities


# Censors profanities using better_profanity functions, which work except when there is @, $, *, ", '
def removeProfanities(text, profanities):
    profanity.load_censor_words(profanities)
    textCorrected = profanity.censor(text)
    return textCorrected

# Get text from file
def getFileText(fileName):
    try:
        file2correct = open(os.path.dirname(__file__) + "\\..\\files\\" + fileName, "r", encoding='utf-8')
        text = file2correct.read()  # get the full html file
        file2correct.close()
        return text
    except FileNotFoundError:
        print("File \"" + file2correctName + "\" not found in Files folder")
        exit()

# Get profanities from list
profanities = getProfanities("\\..\\files\\bannedWords.txt")  # HERE we specify the file with the words #

# Get text from file
text = getFileText(file2correctName)

# Censor the profanities
text = removeProfanities(text, profanities)

# Save the changes in a new file
f = open(os.path.dirname(__file__) + "\\..\\correctedFiles\\" + correctedFileName, "w")
f.write(text)
f.close()
