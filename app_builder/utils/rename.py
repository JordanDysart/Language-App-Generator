#!/usr/bin/python3

# rename.py
#
# Author  : jordan dysart
# Date    : January 16, 2020
# Version : 0.1.0 
#
# Purpose : provide utility functions for finding where our assets are

def getPathTo(here):
    '''
    join an array together to form a string that represents a path
    '''
    return '/'.join(here)

def idAudioFile(name):
    '''
    take a file name and see if it is an audio file return bool
    this can only take one name at a time it will queue our copy method
    '''
    isAudio = False
    file_extensions = ('.mp3', '.flac', '.wav')
    if (name.lower().endswith(file_extensions)):
        isAudio = True
    return isAudio

def makeAndroidFileName(*args):
    '''
    take a name change it to lowercase and strip out illegal symbols
    '''
    symbols = ["(", ")", "?"]
    name = [word.lower() for word in args]
    name = [word.replace(' ', '_') for word in name]
    name = [removeSymbols(word, *symbols) for word in name]
    return '_'.join(name)
    
def removeSymbols(name, *args):
    '''
    @param{name} string
    @param{args} string[]
    remove all specified args from name
    '''
    for symbol in args:
        name = name.replace(symbol, '')

        # name = name.strip(symbol)
    return name

def makeDisplayName(name):
    '''
    create a pretty name that would display on screen
    '''
    file_extension = ['.mp3','.flac','.wav']
    name = removeSymbols(name, *file_extension)
    return name


    


