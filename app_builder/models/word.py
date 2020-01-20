#!/usr/bin/python3

# word.py
#
# Author  : jordan dysart
# Date    : January 16, 2020
# Version : 0.1.0 
#
# Purpose : object representation of our word
# Note    : This file will hold reference to the word and filename (for audiofile)


from app_builder.utils.rename import makeDisplayName, makeAndroidFileName

class Word:

    def __init__(self, filename):
        self.filename = filename
        self.android_filename = makeAndroidFileName(filename)
        self.display_name = makeDisplayName(filename)

    def setAndroidFilename(self, android_filename):
        self.android_filename = android_filename
    
    def getAndroidFilename(self):

        return self.android_filename

    def setDisplayName(self, display_name):
        self.display_name = display_name

    def getDisplayName(self):

        return self.display_name

 
        