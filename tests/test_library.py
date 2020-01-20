#!/usr/bin/python3

# test_word.py
#
# Author  : jordan dysart
# Date    : January 17, 2020
# Version : 0.1.0 
#
# Purpose : Test the Word object and functions

import unittest, context

from app_builder.models.word import Word
from app_builder.models.category import Category
from app_builder.models.library import Library

class LibraryTest(unittest.TestCase):

    def setUp(self):
        audio_file = 'January.mp3'
        word = Word(audio_file)
        self.category = Category('Months')
        self.category.addWord(word)
        audio_file = 'February.mp3'
        word = Word(audio_file)
        self.category.addWord(word)

        self.library = Library()
        self.library.addCategory(self.category)


    def test_library_get_category_dictionary(self):
        
        self.assertEqual({'Months' :{\
            'January':'january.mp3',\
            'February':'february.mp3'\
            }}, self.library.getLibrary())
        # self.assertEqual('january.mp3', word.getAndroidFileName())


    


if __name__ == "__main__":
    unittest.main()