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
from unittest import mock

# replace these, and mock them
from os.path import isfile, join
from os import getcwd



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
        library = Library()
        for category in categories:
            library.addCategory(category)
            for word in words:
                category.addWord(word)
        self.tw = TemplateWriter(library)
        self.testtemplate = "tests/test_template.txt"

    def test_template_filename(self):
        '''
        TODO: change this guy, the test depends on whether or not a file exists.
        '''
        self.assertEqual(True, self.tw.templateExists('testfile.txt'))
        self.assertEqual(False, self.tw.templateExists('doesnotexist.txt'))

    def test_template_with_integer(self):
        self.assertEqual(False, self.tw.templateExists(123))

    def test_copy_template_to_output(self):
        output_file = 'outfile.java'
        output_file_path = join(OUTPUT_DIR, output_file)

        input_file = 'testfile.txt'
        if self.tw.templateExists(input_file):
            self.tw.copyTemplateToOutput(input_file,output_file)
        self.assertEqual(True, isfile(output_file_path))

    def test_check_line_false(self):
        test_line = 'import java.util.Collections;'
        self.assertEqual(None, self.tw.checkLine(test_line))

    def test_check_line_true(self):
        test_line = "{{[f'R.raw.{icon},' for icon in icons]}}"
        self.assertIsNot(None,self.tw.checkLine(test_line))
    
    def test_plan_work(self):

        test_line = "{{[f'{category},' for category in categories]}}"
        self.assertEqual(None, self.tw.planWork(1,test_line))

    def test_get_work_category(self):
        category = Category("test_work")
        library = Library()
        library.addCategory(category)
        template_writer = TemplateWriter(library)
        test_data = ['6',"categories"]
        template_writer.planWork(*test_data)

        expected_result = '"test_work",\n\t\t'
        self.assertEqual(expected_result, template_writer.prepLibrary())

    def test_get_work_category_content(self):
        category = Category("test_work")
        word = Word('Jordan.mp3')
        
        category.addWord(word)
        word = Word('Dysart.mp3')
        category.addWord(word)
        library = Library()
        library.addCategory(category)
        template_writer = TemplateWriter(library)
        test_data = ['6',"words"]
        template_writer.planWork(*test_data)

        expected_result = '"jordan",\n\t\t"dysart",'
        self.assertEqual(expected_result, template_writer.prepLibrary())


        
    # def test_get_work_category_content_audio(self):
    #     category = Category("test_work")
    #     word = Word('jordan')
    #     category.addWord(word)
    #     word = Word('dysart')
    #     category.addWord(word)
    #     library = Library()
    #     library.addCategory(category)
    #     template_writer = TemplateWriter(library)
    #     test_data = ['6',"audio"]
    #     template_writer.planWork(*test_data)

        

if __name__ == "__main__":
    unittest.main()

# Garbage Dump


        # output_file = path.join(getcwd(), self.testtemplate)
        
        # with open(output_file, 'r') as template:
        #     for num, line in enumerate(template):
        #         print(line, end='')
        #         match = self.tw.checkLine(line)
        #         if match != None:
        #             self.tw.planWork(num, match.group(1))
        #             break
            
        #     with open(WORK_FILE, 'r') as work:
        #         self.assertEqual('12 List<Categories>\n', work.readline())