import requests
import json
import time
import sys

from functions import return_to_menu

#remove https warning
requests.packages.urllib3.disable_warnings()

#Define variable
status_code = 0

#Start of function
print ("\n")
#Scan file method
def check_uploaded(api_key, url):
    #Menu Options
    selection=True
    while selection:
        print ("Select option: \n")
        print("""
        1. Check Status of One File
        2. Import Threat Emulation Report
        3. Exit/Quit
        """)
        selection=input("Select a task number: ")
        if selection=="1":
            #Prompt User for MD5Hash
            md5sum = input("Enter the MD5 sum: ")
            file = ""
            check(api_key, url, md5sum, file)
            break
        elif selection=="2":
            #Get Path to file
            path = input("Enter the file you wish to import. Use forward slashes, even on Windows: ")
            md5result = []
            substr = "Info to check results: "
            while True:
                try:
                    inFile = open(path)
                except: 
                    print ("There was an error, please check your input")
                    path = input("Enter the file you wish to import. Use forward slashes, even on Windows: ")
                else:
                    break
            
            for line in inFile:
                if line.startswith(substr):
                    #Parse Output and strip out md5 hash
                    md5sum_split = line.split(" ")
                    md5sum = md5sum_split[-1]
                    md5sum = md5sum.strip()
                    file_path = md5sum_split[-2]
                    check(api_key, url, md5sum, file_path)
            break
        elif selection=="3":
            print("\nGoodbye")
            sys.exit() 
            selection = None
        else:
            print("\n Not Valid Choice. Try again.")
    return_to_menu()
    #Prompt user for file path
    
 
    
    
def check(api_key, url, md5sum, file_path):       
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
        print ("\n")
        print ("Checking Status for: " + file_path)
        response = requests.post(url+"query", json=data, headers=headers, verify=False)
        response_json = json.loads(response.content)
        status_code = response_json['response'][0]['status']['code']
        print ("\n")    
        print ("Message: " + response_json['response'][0]['status']['message'])
        print ("\n")
        print ("Threat Emulation Results:")
        print ("Verdict: " + response_json['response'][0]['te']['images'][0]['report']['verdict'])
        print ("Status: " +response_json['response'][0]['te']['images'][0]['status'])
        print ("\n")
        print ("Anti-Virus Results:")
        print ("Message: " + response_json['response'][0]['av']['status']['message'])
        av_label = response_json['response'][0]['av']['status']['label']
        print ("Label: " + av_label)
        if av_label == "FOUND":
            print ("Signature Name: " + response_json['response'][0]['av']['malware_info']['signature_name'])
            print ("Severity: " + str(response_json['response'][0]['av']['malware_info']['severity']))
            print ("Confidence: " + str(response_json['response'][0]['av']['malware_info']['confidence']))
        print ("\n")
    except:
        print ("Query Failed. Please try again.")
    
