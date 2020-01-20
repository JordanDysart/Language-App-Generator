#!/usr/bin/python3

# category.py
#
# Author  : jordan dysart
# Date    : January 16, 2020
# Version : 0.1.0 
#
# Purpose : object representation of our category

class Library:

    def __init__(self):
        self.categories = []

    def addCategory(self, category):
        self.categories.append(category)

    def getCategory(self):

        return [category.getTitle() for category in self.categories ]

    def getLibrary(self):
        library = {}
        for category in self.categories:
            library[category.getTitle()] = category.getCategoryDictionary()
            
        return library

    

    

