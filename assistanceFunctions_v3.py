"""
Authors: Justin Pusztay and Trevor Stalnaker
File: assistantFunctions_v3.py
Version 3
"""

from urllib.request import *
from urllib.error import *
from webbrowser import *
import os
import subprocess
from weatherStats import WeatherStats

search_Terms_Dict = {"GOOGLE" : "GOOGLE", "SEARCH FOR" : "FOR", \
                     "LOOK UP" : "UP", "FIND" : "FIND"} 
open_Terms_List = ["OPEN", "RUN"]

"""
A function that removes unwanted characters from a sentence.
"""
def characterRemover(sentence):
    for character in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?",\
                      ">","<",".",","]:
        sentence = sentence.replace(character, "")
    return sentence

"""
A function that standardizes a given sentence into all upper case and splits
the sentence word by word into a list. 
"""
def sentenceStandardizer(sentence):
    sentence_list = characterRemover(sentence.upper()).split()
    return sentence_list

"""
A function that can search google for anything a user inputs
"""
def googleSearch(string):
    string = "http://www.google.com/#q="+string.replace(" ","+")
    open_new(string)
    
"""
Prints the weather of a given location
"""
def getWeather(location):
    w = WeatherStats(location)
    return w

"""
A function that finds a location in given sentence.
If there is no location provided, it provides a default.
"""


#This function needs to be changed, add zip codes and GPS coordinates.
#This is where machine learning program comes in
def getLocation(sentence):
    wordLyst = sentenceStandardizer(sentence)
    if "IN" in wordLyst:
        in_position = wordLyst.index("IN")
        location_position = in_position + 1
        location = wordLyst[location_position]
    
    else:
        location = "Natural_Bridge"
    return location

"""
A function that finds the search terms in a given sentence
"""
def getSearchTerms(sentence, keyWord):
    wordLyst = sentenceStandardizer(sentence)
    googlePosition = wordLyst.index(keyWord)
    startPosition = googlePosition + 1
    searchTerms = ""
    for i in range(startPosition, len(wordLyst)):
        searchTerms += wordLyst[i]
        searchTerms += " "
    return searchTerms

"""
Opens a given program and automatically attaches '.exe'
"""
file_end_types = [".exe", ".txt", ".java"]
def openProgram(program):
    if program == "MINECRAFT":
        os.startfile("C:\Program Files (x86)\Minecraft\MineCraftLauncher")
    elif program == "PLANTSVSZOMBIES":
        os.startfile("C:\Program Files (x86)\PopCap Games\Plants vs. Zombies\PlantsVsZombies")
    elif program == "MONOPOLY":
        os.startfile("C:\Program Files (x86)\PopCap Games\Monopoly\monopolywin")
    elif program == "LIFE":
        os.startfile("C:\Program Files (x86)\PopCap Games\The Game of Life\The Game of Life")
    else:
        for fileType in file_end_types:
            try:
                program += fileType
                os.startfile(program)
            except:
                s = 0 #An arbitrary line of code that prevents red ink
                      #May be changed in future versions

"""
Finds a program to run within a given string
"""
def findProgram(sentence, keyword):
    wordLyst = sentenceStandardizer(sentence)
    openPosition = wordLyst.index(keyword)
    programPosition = openPosition + 1
    return wordLyst[programPosition]
    
    

"""
Checks user input for various parameters and acts on them.

Inputs are given precidence based on their position in the function.
i.e. Higher input checks have higher precidence and will be evaluated if
a conflict arises.
"""
def checkInput(user_input):

    #Checks input to determine if user wants a google search on a topic
    for key in search_Terms_Dict:
        if key in user_input:
            googleSearch(getSearchTerms(user_input, search_Terms_Dict[key]))
            return None
        
    #Checks input to determine if user wants weather data
    if "WEATHER" in user_input:
        return str(getWeather(getLocation(user_input)))

    #Checks input to determine if user wants to run an application
    for element in open_Terms_List:
        if element in user_input:
            openProgram(findProgram(user_input, element))
            return None

    
    
