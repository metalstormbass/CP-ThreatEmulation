#!/bin/python

import requests
import json
import pprint
import sys
import time
import hashlib
import httplib
import os.path
import ssl

from functions import md5
from functions import file_name

#remove https warning
requests.packages.urllib3.disable_warnings()

def scanfile(api_key, url, te_cookie):
    file_path = raw_input("Enter full file path (Use forward slashes, even in Windows): ")
    
    
    
    data = '''
    
    {
        "request": [
            {
                "md5": "'''+ md5(file_path) +'''",
                "features": [
                "te",
                "av"
                "extraction"
                ],
                "file_name":  "'''+ file_name(file_path) +'''"
                "te": {
                "reports": [
                    "xml",
                    "pdf"
                ]
                }
                "extraction": {
                "method": "pdf"
                }
            }
        ]
    }
    '''
    data_json = json.dumps(data)
    headers = {
            "User-Agent": "python-api-wrapper",
            "Accept": "*/*",
            "Content-Type": "application/json", 
            "Content-Length": len(data),
            "Authorization": api_key,
            "te_cookie": te_cookie
        }
    
    print data_json
    print data
    print headers
    
    #response = requests.post(url+"query", json=data_json, headers=str(headers), verify=False)
    #print response
    