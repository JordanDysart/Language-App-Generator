#!/usr/bin/python3

# category.py
#
# Author  : jordan dysart
# Date    : January 16, 2020
# Version : 0.1.0 
#
# Purpose : object representation of our category

class Category:

    def __init__(self, title):
        self.title = title
        self.words = []

    def setIsCategory(self, is_category):
        self.is_category = is_category

    def isCategory(self):
        return self.is_category
    
    def getTitle(self):
        return self.title

    def addWord(self, word):
        self.words.append(word)

    def getWords(self):
        return self.words

    def printWords(self):
        return [word.getDisplayName() for word in self.words]

    def printFilenames(self):
        return [word.getAndroidFilename() for word in self.words]

    def getCategoryDictionary(self):
        category = {}
        for word in self.words:
            category[word.getDisplayName()] = word.getAndroidFilename()
        return category

