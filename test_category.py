#!/usr/bin/python3

# test_category.py
#
# Author  : jordan dysart
# Date    : January 16, 2020
# Version : 0.1.0 
#
# Purpose : Test Category object & functions

import unittest

from category import Category
from word import Word


class CategoryTests(unittest.TestCase):

    def setUp(self):
        audio_file = 'January.mp3' 
        word = Word(audio_file)
        self.category = Category('Months')
        self.category.addWord(word)
        
    def test_get_word(self):
        
        self.assertEqual(['January'], self.category.printWords())

    def test_get_android_filename(self):
        audio_file = 'December.flac' 
        word = Word(audio_file)
        self.category.addWord(word)
        self.assertEqual(['january.mp3', 'december.flac'], self.category.printFilenames())

    def test_get_category_dictionary(self):
        category = self.category
        self.assertDictEqual({'January': 'january.mp3'}, category.getCategoryDictionary())

    def test_get_category_dictionary_with_more(self):
        category = self.category
        audio_file = 'December.flac' 
        word = Word(audio_file)
        category.addWord(word)
        self.assertDictEqual({\
            'January': 'january.mp3',\
            'December':'december.flac'\
            }, category.getCategoryDictionary())
        


    


if __name__ == "__main__":
    unittest.main()