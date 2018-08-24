#!/bin/python
import sys

from scanfile import scanfile
from check_quota import check_quota

def menu(): 
    #Variables
    url = "https://te.checkpoint.com/tecloud/api/v1/file/"
    api_key = raw_input("Enter your Check Point Threat Emulation API key: ")
    #Menu Options
    selection=True
    while selection:
        print "Select option: \n"
        print("""
        1. Check Threat Emulation Quota Status
        2. Scan a file
        3. Scan a directory - Function still in development
        4. Exit/Quit
        """)
        selection=raw_input("Select a task number: ")
        if selection=="1":
          print("\nCheck Threat Emulation Quota Status")
          check_quota(api_key, url)
        elif selection=="2":
          print("\nScan a file")
          scanfile(api_key, url)
        elif selection=="3":
          print("\nScan a directory - Function still in development")
        elif selection=="4":
          print("\nGoodbye")
          sys.exit() 
          selection = None
        else:
           print("\n Not Valid Choice Try again")