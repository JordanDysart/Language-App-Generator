#!/usr/bin/python3

# test_rename.py
#
# Author  : jordan dysart
# Date    : January 16, 2020
# Version : 0.1.0 
#
# Purpose : Test the functions built in rename

import unittest, context

from app_builder.utils.rename import *

class TestGetPath(unittest.TestCase):

    def test_get_path_to_cwd(self):
        self.assertEqual('.', getPathTo('.'))

    def test_get_path_to_dir(self):
        dst = ['.', 'Audio']
        self.assertEqual('./Audio', getPathTo(dst))
    
    def test_get_path_to_file(self):
        dst = ['.', 'Audio', 'file.mp3']
        self.assertEqual('./Audio/file.mp3', getPathTo(dst))

    def test_get_path_to_empty_array(self):
        dst = []
        self.assertEqual('', getPathTo(dst))

class TestIdFile(unittest.TestCase):

    def test_id_file_type_success(self):
        testfile = 'one.mp3'
        self.assertEqual(True, idAudioFile(testfile))

    def test_id_file_type_failure(self):
        testfile = 'one.mp4'
        self.assertEqual(False, idAudioFile(testfile))

class TestAndroidFileName(unittest.TestCase):

    def test_make_android_filename(self):
        category = 'Months'
        word = 'January.mp3'
        self.assertEqual('months_january.mp3', makeAndroidFileName(category, word))

    def test_make_android_filename_with_spaces(self):
        category = 'Days of the week'
        word = 'Monday.mp3'
        self.assertEqual('days_of_the_week_monday.mp3', makeAndroidFileName(category, word))

    def test_make_android_filename_with_symbols(self):
        category = 'Questions'
        word = 'Ask him (her)?.mp3'
        self.assertEqual('questions_ask_him_her.mp3', makeAndroidFileName(category, word))

class TestRemoveSymbols(unittest.TestCase):

    def test_remove_symbol(self):
        symbols = ["(", ")", "?"]
        word = 'Ask him (her)?.mp3'
        self.assertEqual('Ask him her.mp3', removeSymbols(word, *symbols))

    def test_remove_symbol_for_invalid_file_extension(self):
        '''
        TODO: This should be stripping out everything that is asked but there should be
        a way to create a valid filename... right... maybe...
        '''
        symbols = [".mp3", ".flac", ".wav"]
        word = 'Ask him (her)?.mp3.mp3'
        self.assertEqual('Ask him (her)?', removeSymbols(word, *symbols))
        # self.assertEqual('Ask him (her)?.mp3', removeSymbols(word, *symbols))

class TestMakeDisplayName(unittest.TestCase):

    def test_make_display_name(self):
        filename = 'Ask him (her)?.mp3'
        self.assertEqual('Ask him (her)?', makeDisplayName(filename))

    
if __name__ == "__main__":
    unittest.main()