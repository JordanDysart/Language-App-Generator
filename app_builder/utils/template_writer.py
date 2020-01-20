#!/usr/bin/python3

# template_writer.py
#
# Author  : jordan dysart
# Date    : January 19, 2020
# Version : 0.1.0 
#
# Purpose : utilities for writing a data file
#
# Remarks : Doing it myself, we will write line by line. I'll follow the jinja2 template
# engine whenever I can.
# Also, why don't I just copy the template into output and replace lines directly
# in the one file.

from os import path, getenv
from shutil import copyfile

PROJECT_DIR  = getenv('PROJECT_DIR')
APP_DIR      = 'app_builder/'
OUTPUT_DIR   = path.join(PROJECT_DIR, APP_DIR, 'output/')
TEMPLATE_DIR = path.join(PROJECT_DIR, APP_DIR, 'templates/')


input_file = None

def setInputFileName(filename):
    '''
    set the input path name
    '''
    input_file = path.join(TEMPLATE_DIR, str(filename))
    return path.isfile(input_file)

def copyTemplateToOutput(filename):
    if input_file:
        output_file = path.join(OUTPUT_DIR, filename)
        copyfile(input_file, output_file)
        output_file = None


def checkLine(line):
    '''
    take a line from a filereader and test if there is template placeholder
    {% like this %}. If there is start parsing the text inside.
    '''
    return False
    



