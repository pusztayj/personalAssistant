"""
File: smartImport.py
Author: Trevor Stalnaker
Version 1

A program that allows clients to import the newest version of a module
automatically rather than manually.

Files using this program must be written in the form: <File Name>_v<Version Number>
"""

import os


#This is a new comment
"""
Using the above described format, this function searches for the newest
version of a provided software and returns it as a string.
"""
def smartImport(moduleName):
    
    module = moduleName
    file_list = os.listdir(os.getcwd())
    
    possible_files = []
    for file in file_list:
        if module in file:
            possible_files.append(file)

    versionNumber = 0
    for file in possible_files:
        underScorePosition = file.index("_")
        if int(file[underScorePosition + 2]) >= versionNumber:
            versionNumber = int(file[underScorePosition + 2])
            
    string = module + "_v" + str(versionNumber)
    return string

