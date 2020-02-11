import datetime
import requests
import json
import time
import os

from functions import md5
from functions import file_name
from functions import return_to_menu
from functions import file_extension



#Define Global Variable
status_code = 0


def scan_directory(api_key, url, file_path, report_path, rname):
    #Open file and write to report
    f = open(report_path + rname, "a")
    
    #Parse Input and perform error checking 
    while True:
        try:
            md5sum =md5(file_path)
        except: 
            f.write(file_path + " does not exist or has a problem with it.")
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
    
    try:
        #Define Global variable
        global status_code
        print ("\n")
        print ("Scanning " + file_path)
        response = requests.post(url+"query", json=data, headers=headers, verify=False)
        response_json = json.loads(response.content)
        status_code = response_json['response'][0]['status']['code']
        av_label = response_json['response'][0]['av']['status']['label']
        
        f.write("Results for " + file_path + "\n")
        f.write('Message: ' + response_json['response'][0]['status']['message']+'\n')
        f.write('Threat Emulation Results: \n\n')
        f.write('Verdict: ' + response_json['response'][0]['te']['images'][0]['report']['verdict']+'\n')
        f.write('Status: ' +response_json['response'][0]['te']['images'][0]['status']+'\n')
        f.write('Anti-Virus Results: \n\n')
        f.write('Message: ' + response_json['response'][0]['av']['status']['message']+'\n')
        f.write('Label: ' + av_label +'\n')
        
        if av_label == "FOUND":
            f.write('Signature Name: ' + response_json['response'][0]['av']['malware_info']['signature_name'] +'\n')
            f.write('Severity: ' + str(response_json['response'][0]['av']['malware_info']['severity']) +'\n')
            f.write('Confidence: ' + str(response_json['response'][0]['av']['malware_info']['confidence']) +'\n')
        f.write("Info to check results: "+ file_path + " " + md5sum +'\n\n\n')    
            
    except:
        f.write(file_path + ' Encountered and error. Results not available" \n')
    
    f.write('\n')
    f.write('\n')
    
   
    #Checking to see if user wants to upload file.
    if status_code == 1004:
        #Retrieve Extension
        file_ext=file_extension(filename)
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
        try:
            response = requests.post(url+"upload", headers = headers, files=files)
            response_json = json.loads(response.content)
            f.write('Upload_Status: ' + response_json['response']['status']['message'] +'\n')
        except: 
            f.write('There was a problem when uploading the file')
        
    f.close()    

    

def get_directory(api_key, url):
    #Initialize Arrays
    fn = []
    
    
    print ("\nThis function will scan a directory and upload any unknown files. \n")
    path = input("Enter directory to scan(Use forward slashes, even in Windows): ")
    if not path.endswith("/"):
        path = path + "/"   
    report_path = input("Enter directory to save report (Use forward slashes, even in Windows): ")  
    if not report_path.endswith("/"):
        report_path = report_path + "/" 
    
    rname = "report" + datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S") + ".txt"
    f = open(report_path + rname, "w+")
    f.write("Threat Emulation Report \n\n")
    f.close()  

    #Scan Recursively
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            ftemp = os.path.join(root, name)
            ftemp = ftemp.replace('\\', '/')
            fn.append(ftemp)
        for name in dirs:
            temp = os.path.join(root, name)
            ftemp = ftemp.replace('\\', '/')
            fn.append(ftemp)
    i = 0
    for filenames in fn:
        file_path = fn[i]
        scan_directory(api_key, url, file_path, report_path, rname)
        i += 1
        
        
    print ("\n")
    print ("Report stored in: " + report_path + rname)
    print ("\n")
    return_to_menu()


