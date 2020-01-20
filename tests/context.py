#!/usr/bin/python3

# context.py
#
# Author  : jordan dysart
# Date    : January 19, 2020
# Version : 0.1.0 
#
# Purpose : Provide context to tests now that they are separated.

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app_builder
#print(help('modules builder')) # neat way to find modules available

