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
    
    print filename
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
    
    files = {
     'json': (None, json.dumps(data), 'application/json'),
     'file': (filename, open(file_path, 'rb'), 'application/octet-stream')
    }
    #Assemble the header
    headers = {"Authorization": api_key}
    
    #send request
    response = requests.post(url+"upload", headers = headers, files=files)
    response_json = json.loads(response.content)
    print "\n"
    print "Message: " + response_json['response']['status']['message']
    print "\n"
    print "Make note of the MD5 sum to check progress: " + md5sum