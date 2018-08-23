#!/bin/python

import requests
import json
import time


from functions import md5
from functions import file_name

#remove https warning
requests.packages.urllib3.disable_warnings()
print "\n"
#Scan file method
def scanfile(api_key, url):
    file_path = raw_input("Enter full file path (Use forward slashes, even in Windows): ")
   
    #Parse Input from user and place into JSON request
    md5sum =md5(file_path)
    filename=file_name(file_path)
    
    data ={
        "request": [
            {
                "md5": md5sum,
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
        
    #Assemble the heaer
    headers = {"User-Agent": "python-api-wrapper", "Accept": "*/*","Content-Type": "application/json", "Content-Length": str(len(data)),"Authorization": api_key}
    
    #Send the request and parse the reply
    
    try:
        print "Scanning Now..."
        response = requests.post(url+"query", json=data, headers=headers, verify=False)
        response_json = json.loads(response.content)
        print "\n"
        print "\n"    
        print "\n"
        print "Message: " + response_json['response'][0]['status']['message']
        print "\n"
        print "Threat Emulation Results:"
        print "Verdict: " + response_json['response'][0]['te']['images'][0]['report']['verdict']
        print "Status: " +response_json['response'][0]['te']['images'][0]['status']
        print "\n"
        print "Anti-Virus Results:"
        print "Message: " + response_json['response'][0]['av']['status']['message']
        print "Label: " + response_json['response'][0]['av']['status']['label']
        print "\n"
        print "\n"    
        print "\n"
    except:
        print "Query Failed. Please try again."