#!/bin/python

import requests
import json
import time


from functions import md5
from functions import file_name
from functions import return_to_menu
from upload import upload

#remove https warning
requests.packages.urllib3.disable_warnings()

#Define variable
status_code = 0

#Start of function
print "\n"
#Scan file method
def scanfile(api_key, url):
    #Prompt user for file path
    file_path = raw_input("Enter full file path (Use forward slashes, even in Windows): ")
       
    #Parse Input and perform error checking 
    while True:
        try:
            md5sum =md5(file_path)
        except: 
            print "There was an error, please check your input"
            file_path = raw_input("Enter full file path (Use forward slashes, even in Windows): ")
        else:
            break

    filename=file_name(file_path)
    
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
    
    #try:
    #Define Global variable
    global status_code
    print "\n"
    print "Scanning Now..."
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
        print "Confidence: " + str(response_json['response'][0]['av']['status']['confidence'])
    print "\n"
    #except:
     #   print "Query Failed. Please try again."
   
'''
    #Checking to see if user wants to upload file.
    if status_code == 1004:
        print "Would you like to upload your file for emulation?"

        print("""
        1.Upload file for emulation
        2.Do not upload file
        """)
        selection=raw_input("Select a task number: ")
        if selection=="1":
          print "\nUpload File"
          upload(api_key, url, file_path, md5sum, filename)
        elif selection=="2":
          print("\n")
          return_to_menu
          selection = None
        else:
           print("\n Not Valid Choice Try again")

    print "\n"
    return_to_menu()
'''    