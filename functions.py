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
    print ("Return to main menu?")
    print("""
    1. Return to main menu
    2. Exit/Quit
    """)
    selection=input("Select a task number: ")
    if selection=="1":
        print ("\n")

        print('''
   ____ _               _      ____       _       _                                
  / ___| |__   ___  ___| | __ |  _ \ ___ (_)_ __ | |_                              
 | |   | '_ \ / _ \/ __| |/ / | |_) / _ \| | '_ \| __|                             
 | |___| | | |  __/ (__|   <  |  __/ (_) | | | | | |_                              
  \____|_| |_|\___|\___|_|\_\ |_|   \___/|_|_| |_|\__|                             
  _____ _                    _     _____                 _       _   _             
 |_   _| |__  _ __ ___  __ _| |_  | ____|_ __ ___  _   _| | __ _| |_(_) ___  _ __  
   | | | '_ \| '__/ _ \/ _` | __| |  _| | '_ ` _ \| | | | |/ _` | __| |/ _ \| '_ \ 
   | | | | | | | |  __/ (_| | |_  | |___| | | | | | |_| | | (_| | |_| | (_) | | | |
   |_| |_| |_|_|  \___|\__,_|\__| |_____|_| |_| |_|\__,_|_|\__,_|\__|_|\___/|_| |_|''')                                                                                                         
        print ("\n")
        print ("V 1.1 - Written by Michael Braun")
        print ("\n")
        return
    elif selection=="2":
          print("\nGoodbye")
          sys.exit() 
          selection = None
    else:
           print("\n Not Valid Choice. Try again.")
    
