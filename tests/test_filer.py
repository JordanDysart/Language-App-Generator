#!/usr/bin/python3

# test_filer.py
#
# Author  : jordan dysart
# Date    : January 19, 2020
# Version : 0.1.0 
#
# Purpose : Test filer.py

# Remarks : This is being built for android java right now

import unittest, context

from os.path import isfile, join

from app_builder.utils.template_writer import *
from app_builder.models.word import Word
from app_builder.models.category import Category
from app_builder.models.library import Library


class FilerTests(unittest.TestCase):

    def setUp(self):
        '''
        create a library to use for these tests.
        '''
        words = [ Word(f"word_{count+1}") for count in range(10) ]
        categories = [ Category(f"category_{count+1}") for count in range(10) ]
        self.library = Library()
        for category in categories:
            self.library.addCategory(category)
            for word in words:
                category.addWord(word)

    def test_set_input_filename(self):
        self.assertEqual(True, setInputFileName('testfile.txt'))
        self.assertEqual(False, setInputFileName('doesnotexist.txt'))

    def test_set_input_with_integer(self):
        self.assertEqual(False, setInputFileName(123))

    def test_copy_template_to_output(self):
        output_file = 'outfile.java'
        output_file_path = join(OUTPUT_DIR, output_file)

        self.assertEqual(False, isfile(output_file_path))
        setInputFileName('testfile.txt')
        copyTemplateToOutput(output_file)
        self.assertEqual(True, isfile(output_file_path))
        if (isfile(output_file_path) and False):
            from os import remove
            remove(output_file_path)


    def test_check_line(self):
        test_line = 'import java.util.Collections;'
        self.assertEqual(False, checkLine(test_line))
    
   
        




if __name__ == "__main__":
    unittest.main()