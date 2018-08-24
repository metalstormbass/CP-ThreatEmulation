#!/bin/python

import requests
import json
import time

from functions import return_to_menu
from functions import file_extension

#remove https warning
requests.packages.urllib3.disable_warnings()

def upload(api_key, url, file_path, md5sum, filename):
    #Retrieve Extension
    file_ext=file_extension(filename)
    print file_ext
    
    #Input variables into JSON
    data ={
    "request": {
        "md5": md5sum,
        "file_name": filename,
        "file_type": file_ext,
        "features": ["te"],
        "te": {
            "reports": ["pdf", "xml"],
            "images": [
                {
                    "id": "7e6fe36e-889e-4c25-8704-56378f0830df",
                    "revision": 1
                },
                {
                    "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
                    "revision": 1
                }
            ]
        }
    }
    }

    #Assemble the header
    headers = {"User-Agent": "python-api-wrapper", "Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","Authorization": api_key}
    
    
    #with open(file_path, 'rb') as f:
    #    response = requests.post(url+"upload", headers = headers, files={file_path: f})