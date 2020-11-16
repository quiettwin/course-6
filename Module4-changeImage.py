#! /usr/bin/env python3

from PIL import Image
from pathlib import Path
import os

path = "~/supplier-data/images"
size = 600, 400

def convertImage():
    # Search the path for root, directories, and files.
    for root, dirs, files in os.walk(path, topdown=True):
        # For each file found, check that it has the extension ".tif"
        for inFile in files:
            fileName, extension = os.path.splitext(files)
            if extension == ".tif":
                # If the file is a ".tif" open it, then convert and save it as a ".jpeg"
                try:
                    with Image.open(inFile) as newImage:
                        newImage.size(size).convert("RGB").save(path + "/" + fileName, "JPEG" )
                # If the file is not a ".tif" raise an OSError stating the file is unable to be converted.
                except OSError:
                    print("Cannot convert ", inFile)