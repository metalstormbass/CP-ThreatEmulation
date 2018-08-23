#!/bin/python

from scanfile import scanfile
import sys

#Global variables
url = "https://te.checkpoint.com/tecloud/api/v1/file/"
te_cookie = "tec"

print'''
   ____ _               _      ____       _       _                                
  / ___| |__   ___  ___| | __ |  _ \ ___ (_)_ __ | |_                              
 | |   | '_ \ / _ \/ __| |/ / | |_) / _ \| | '_ \| __|                             
 | |___| | | |  __/ (__|   <  |  __/ (_) | | | | | |_                              
  \____|_| |_|\___|\___|_|\_\ |_|   \___/|_|_| |_|\__|                             
  _____ _                    _     _____                 _       _   _             
 |_   _| |__  _ __ ___  __ _| |_  | ____|_ __ ___  _   _| | __ _| |_(_) ___  _ __  
   | | | '_ \| '__/ _ \/ _` | __| |  _| | '_ ` _ \| | | | |/ _` | __| |/ _ \| '_ \ 
   | | | | | | | |  __/ (_| | |_  | |___| | | | | | |_| | | (_| | |_| | (_) | | | |
   |_| |_| |_|_|  \___|\__,_|\__| |_____|_| |_| |_|\__,_|_|\__,_|\__|_|\___/|_| |_|'''                                                                                                          
print "\n"
print "V 1.0 - Written by Michael Braun"
print "\n"
print "\n"

#User input variables
api_key = raw_input("Enter your Check Point Threat Emulation API key: ")

#Menu Options

print "Select option: \n"

selection=True
while selection:
    print("""
    1.Scan a file
    2.Scan a directory
    3.Exit/Quit
    """)
    selection=raw_input("Select a task number: ")
    if selection=="1":
      print("\nScan a file")
      scanfile(api_key, url, te_cookie)
    elif selection=="2":
      print("\nScan a directory - Function still in development")
    elif selection=="3":
      print("\nGoodbye")
      sys.exit() 
      selection = None
    else:
       print("\n Not Valid Choice Try again")