import PyPDF2  # learn more: https://python.org/pypi/PyPDF2
from nltk import word_tokenize
import nltk
import sklearn
import collections
from nltk.corpus import stopwords
#nltk.download('stopwords')
#nltk.download('punkt')
print("Start PDF import...")
# creating an object
file = open("D5100_EN.pdf", "rb")

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

findResultsList = []
findCount = 1

searchPhrase = input("Enter a word or phrase you'd like to search for: ")


def GetStartIndex(findIndex):

    begSent1 = findIndex - pageText[findIndex::-1].find(".")

    startIndex = begSent1 - pageText[begSent1 - 1::-1].find(".")

    return startIndex


def GetLastIndex(findIndex):

    endSent1 = findIndex + pageText[findIndex:].find(".")
    endIndex = endSent1 + pageText[endSent1 + 1:].find(".") + 2

    return endIndex


def FindPhrase(phrase, text):
    findIndex = pageText.lower().find(phrase.lower())
    print(text[GetStartIndex(findIndex):GetLastIndex(findIndex)])


pageText = fileReader.getPage(76).extractText()

FindPhrase(searchPhrase, pageText)

print("We found [{}] {} time(s) in this document\n".format(
    searchPhrase.lower(), findCount))

