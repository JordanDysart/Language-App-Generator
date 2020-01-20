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

class WordTests(unittest.TestCase):

    def test_word_name_init_simple(self):
        audio_file = 'January.mp3'
        word = Word(audio_file)

        self.assertEqual('January', word.getDisplayName())
        self.assertEqual('january.mp3', word.getAndroidFilename())

    def test_word_name_init_invalid_filename(self):
        '''
        TODO: review this later the double .mp3 might break in android studio
        but i'm pretty sure that it would still work on any os
        '''
        audio_file = 'January.mp3.mp3'
        word = Word(audio_file)
        self.assertEqual('January', word.getDisplayName())
        self.assertEqual('january.mp3.mp3', word.getAndroidFilename())

    


if __name__ == "__main__":
    unittest.main()