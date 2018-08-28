#!/bin/python

import requests
import json
import time

from functions import return_to_menu

#remove https warning
requests.packages.urllib3.disable_warnings()

#Define variable
status_code = 0

#Start of function
print "\n"
#Scan file method
def check_uploaded(api_key, url):
    #Prompt user for file path
    md5sum = raw_input("Enter the MD5 sum: ")
       
    #Input user information into JSON
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
        
    #Assemble the header
    headers = {"User-Agent": "python-api-wrapper", "Accept": "*/*","Content-Type": "application/json", "Content-Length": str(len(data)),"Authorization": api_key}
    
    #Send the request and parse the reply
    
    try:
        #Define Global variable
        global status_code
        print "\n"
        print "Checking Status Now..."
        response = requests.post(url+"query", json=data, headers=headers, verify=False)
        response_json = json.loads(response.content)
        status_code = response_json['response'][0]['status']['code']
        print "\n"    
        print "Message: " + response_json['response'][0]['status']['message']
        print "\n"
        print "Threat Emulation Results:"
        print "Verdict: " + response_json['response'][0]['te']['images'][0]['report']['verdict']
        print "Status: " +response_json['response'][0]['te']['images'][0]['status']
        print "\n"
        print "Anti-Virus Results:"
        print "Message: " + response_json['response'][0]['av']['status']['message']
        av_label = response_json['response'][0]['av']['status']['label']
        print "Label: " + av_label
        if av_label == "FOUND":
            print "Signature Name: " + response_json['response'][0]['av']['malware_info']['signature_name']
            print "Severity: " + str(response_json['response'][0]['av']['malware_info']['severity'])
            print "Confidence: " + str(response_json['response'][0]['av']['malware_info']['confidence'])
        print "\n"
    except:
        print "Query Failed. Please try again."
    
    return_to_menu()