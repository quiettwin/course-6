#! usr/bin/env python3

import requests
import os
from pathlib import Path

url = "http://xxx.xxx.xxx.xxx/upload/"
path = "~/supplier-data/images"

def uploadImage():
    for root, dirs, files in os.walk(path, topdown=True):
        for inFile in files:
            if os.path.isfile(inFile):
                fileName, extension = os.path.splitext(inFile)
                if extension == ".jpeg":
                    try:
                        with open(path + "/" + inFile, 'rb') as opened:
                            r = requests.post(url, files={'file': opened})
                    except OSError():


     
