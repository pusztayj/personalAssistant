"""
https://www.dictionaryapi.com/api/v1/references/collegiate/xml/dog?key=4d7f8ee4-c607-427d-b9d4-565706ff9b73
"""

import urllib.request
import json
import xmltodict
import untangle
import xml.etree.ElementTree as ET


word = "cat"

def url_builder(word):
    user_api = '4d7f8ee4-c607-427d-b9d4-565706ff9b73'  
    api = 'https://www.dictionaryapi.com/api/v1/references/collegiate/xml/'     
    full_api_url = api + word + "?key="+ user_api
    return full_api_url

def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    tree = ET.ElementTree(
    print(output)




def main():
    print(url_builder("cat"))
    data_fetch(url_builder("cat"))

if __name__ == "__main__":
    main()
    
