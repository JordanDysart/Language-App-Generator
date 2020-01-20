#!/usr/bin/python3

# transform.py
#
# Author  : jordan dysart
# Date    : January 20, 2020
# Version : 0.2.0 
#
# Purpose : Copy and transform these pesky files from boss

import os, sys
from os import path
from shutil import copyfile
from app_builder.models.category import Category
from app_builder.models.word import Word
from app_builder.models.library import Library

from app_builder.utils.rename import getPathTo, idAudioFile


PROJECT_DIR  = os.getenv('PROJECT_DIR')
APP_DIR      = 'app_builder/'
OUTPUT_DIR   = path.join(PROJECT_DIR, 'output/')
TEMPLATE_DIR = path.join(PROJECT_DIR, APP_DIR, 'templates/')
REXPRESS     = r".*\{\{(.*)\}\}"
WORK_FILE    = path.join(OUTPUT_DIR, "planned_work")

FILE_DIR     = path.join(PROJECT_DIR, 'Audio')

def main( **args ):
    cwd = os.getcwd()
    print(f'we are currently here {cwd}')
    # print(f'{ args }')
    # for key, value in args.items():
        # print(key)
    # active_dir = findDirectory(cwd)
    # print(f"ok let's work with {active_dir}")

    active_dir = FILE_DIR
    library = Library()

    f = open('ouput.txt', 'w+')
    f.write("\tprivate String[] categories = {\n\t")
    for directory in os.listdir(FILE_DIR):
        f.write(f'\t\"{directory}\",\n\t')
    f.write(f"}};\n\t")

    audiof = open('output_filenames.txt', 'w+')
    # Assuming that we are in the correct directory, now we can go through them
    directories = os.listdir(FILE_DIR)
    directories.remove('__pycache__')

    for directory in directories:

        f.write(f"private String[] {directory.lower()}_words = {{\n\t")
        audiof.write(f"private Integer[] {directory.lower()}_audio = {{\n\t")
        # Let's start with finding audio files
        category = Category(directory)
        directory_path = getPathTo([FILE_DIR, directory])
        # Let's go through each file in here and build the vocabulary
        for audio_file in os.listdir(directory_path):
            
            if (idAudioFile(audio_file)):
                f.write(f'\t\"{audio_file}\",\n\t')
                
                src = path.join(directory_path, audio_file)
                                
                word = Word(audio_file)
                category.addWord(word)
                dst = path.join(OUTPUT_DIR, word.getAndroidFilename())
                audiof.write(f"\tR.raw.{word.getAndroidFilename()},\n\t")
                copyfile(src, dst)
        f.write(f"}};\n\n\n\t")
        audiof.write(f"}};\n\n\n\t")
                


        library.addCategory(category)
        # end of loop let's see what we've got
    f.close()
    audiof.close()
    
    

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