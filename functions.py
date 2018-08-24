#!/bin/python

import hashlib
import sys


#MD5 file hashing
def md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

#File name parsing
def file_name(file_path):
    filename_split = file_path.split("/")
    filename = str(filename_split[-1])
    return filename

#Find file extension
def file_extension(filename):
    file_ext_split = filename.split(".")
    file_ext="."+str(file_ext_split[-1])
    return file_ext

#Function to return to main menu
def return_to_menu():
    print "Return to main menu?"
    print("""
    1. Return to main menu
    2. Exit/Quit
    """)
    selection=raw_input("Select a task number: ")
    if selection=="1":
      print "\n"
      return
    elif selection=="2":
      print("\nGoodbye")
      sys.exit() 
      selection = None
    else:
       print("\n Not Valid Choice Try again")
    
