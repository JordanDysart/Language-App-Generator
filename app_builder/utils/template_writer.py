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

import re

from os import path, getenv
from shutil import copyfile

PROJECT_DIR  = getenv('PROJECT_DIR')
APP_DIR      = 'app_builder/'
OUTPUT_DIR   = path.join(PROJECT_DIR, APP_DIR, 'output/')
TEMPLATE_DIR = path.join(PROJECT_DIR, APP_DIR, 'templates/')
REXPRESS     = r".*\{\{(.*)\}\}"
WORK_FILE    = path.join(OUTPUT_DIR, "planned_work")

class TemplateWriter:

    def __init__(self, library):
        self.library = library
        self.work = []

    def templateExists(self, filename):
        '''
        set the template path name
        '''
        input_file = path.join(TEMPLATE_DIR, str(filename))
        return path.isfile(input_file)

    def copyTemplateToOutput(self, template, output):
        '''
        I'm going to copy the desired tempolate to output before planning or doing work
        '''
        template_file = path.join(TEMPLATE_DIR, template)
        output_file = path.join(OUTPUT_DIR, output)
        copyfile(template_file, output_file)
        output_file = None


    def checkLine(self, line):
        '''
        take a line from a filereader and test if there is template placeholder
        {{} like this }}. return the match, it's None if there is no match
        '''
        expression = re.compile(REXPRESS)
        match = expression.search(line)
        return match

    def planWork(self, line_num, work_found):
        self.work.append(f"{line_num}:{work_found}")
    
    def prepLibrary(self):
        work_string = ''
        for work_order in self.work:
            _, which = work_order.split(':')
            
            if which == "categories":
                for category in self.library.getCategory():
                    work_string += f'\"{category }\",\n\t\t'
            elif which == 'icons':
                work_string += 'do nothing for now\n'
            elif which == 'words':
                self.library.getLibrary()
                
            elif which == 'audio':
                print(self.library.getLibrary())


        return work_string
            
        



    
    



