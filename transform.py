#!/usr/bin/python3

# transform.py
#
# Author  : jordan dysart
# Date    : January 16, 2020
# Version : 0.1.0 
#
# Purpose : Copy and transform these pesky files from boss

import os, sys
from category import Category
from word import Word
from library import Library

from laam.rename import getPathTo, idAudioFile

def main():
    cwd = os.getcwd()
    active_dir = findDirectory(cwd)
    print(f"ok let's work with {active_dir}")

    library = Library()

    # Assuming that we are in the correct directory, now we can go through them
    for directory in os.listdir(active_dir):
        # Let's start with finding audio files
        category = Category(directory)

        # Let's go through each file in here and build the vocabulary
        for audio_file in os.listdir(getPathTo([active_dir,directory])):
            
            if (idAudioFile(audio_file)):
                
                word = Word(audio_file)
                category.addWord(word)

                
        library.addCategory(category)
        # end of loop let's see what we've got
    print(library.getLibrary())
    
    

def findDirectory(cwd):
    '''
    Let's go on a text adventure and find the proper path
    '''
    directory_choices = os.listdir(cwd)
    directory_choices = [filter(dir) for dir in directory_choices]
    for ind, directory in enumerate(directory_choices):
        print(f"[{ind}] {directory}")
    index_choice = int(input("Select a directory : "))

    next_directory = directory_choices[index_choice]
    direction = os.path.join(cwd, next_directory)
    choice = str(input(f'Is this {direction} the right directory? '))
    if (choice[0] == 'n'):
        findDirectory(direction)
    else:
        return direction

def filter(dir):
    '''
    return directory if is directory
    '''
    if (os.path.isdir(dir)):
        return dir

if __name__ == "__main__":
    main()