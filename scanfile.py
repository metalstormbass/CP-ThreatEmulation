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

#Scan file method
def scanfile(api_key, url, te_cookie):
    file_path = raw_input("Enter full file path (Use forward slashes, even in Windows): ")
    
 
   
    data = ''' 
    {
        "request": [
            {
                "md5": "8dfa1440953c3d93daafeae4a5daa326",
                "features": [
                    "te",
                   "av"
                ],
                "te": {
                    "reports": [
                        "xml",
                        "pdf"
                    ]
                }
            },
            {
                "md5": "521c7603a6892171b3b8e912c973ec87",
                "features": [
                    "te",
                   "av"
                ],
                "te": {
                    "reports": [
                        "xml",
                        "pdf"
                    ]
                }
            }
        ]
    }
    '''
    
    data_json = json.loads(data)
    headers = {
            "User-Agent": "python-api-wrapper",
            "Accept": "*/*",
            "Content-Type": "application/json", 
            "Content-Length": len(data),
            "Authorization": api_key,
            "te_cookie": te_cookie
        }
    
    
    response = requests.post(url+"query", json=data_json, headers=str(headers), verify=False)
    print response
    