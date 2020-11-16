#! usr/bin/env python3

import os
import requests
# import json

url = "http://[linux-instance-external-IP]/fruits"
path = "~supplier-data/descriptions/"
allFruit = []

def processText():
    # Search the path for root, directories, and files.
    for root, dirs, files in os.walk(path, topdown=True):
        # For every file found, check for ".txt" extension.
        for inFile in files:
            fruitInfo = {"name": "", "weight": 0, "description": "", "image-name": ""}
            fileName, extension = os.path.splitext(inFile)
            if extension == ".txt":
                # If the file is a ".txt" file, open the file in Read mode and read each line of the file.
                try:
                    with open(inFile, "r") as opened:
                        Lines = opened.readlines()
                        # For every line in the file, complete the fruitInfo dictionary accordingly.
                        for line in Lines:
                            fruitInfo["name"] = line[0]
                            fruitInfo["weight"] = line[1]
                            fruitInfo["description"] = line[2]
                            fruitInfo["image-name"] = line[3]
                    # Add the fruit information to the allFruit list.
                    allFruit.append(fruitInfo)
                # If the file is NOT a ".txt" file, raise OSError printing to the user that the file cannot be converted.
                except OSError:
                    print("Cannot convert: " + inFile)
    # Upload the fruit dictionaries as JSON to the provided web address for the Django server.            
    r = requests.post(url, json=allFruit)

            