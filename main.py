from SaveImages import SaveImages
from SendImages import SendImages
from GetReplies import GetReplies
from Settings import Settings
from PrintTools import *
import os.path
from os import path
import shutil,json

print("\n\n\n\n\n\n\n\n\n\n\n")

def checkConfig():
    with open('config.json', "r") as f:
        config = json.load(f)
    for key, value in config.items():
        if value =="":
            return False
    return True

if not path.exists("config.json"):
    shutil.copyfile("config-default.json", "config.json")
    PrintBox("New config created, please edit config.json")
    userinput = "5"
elif not checkConfig():
        PrintBox("Empty field detected, please edit config.json")
        userinput = "5"
else:
    # diaplay intial menu
    userinput = menu()


while userinput != "5":
    # Option 1 - Read tweet replies
    # ═══════════════════════════════════════════ 
    if userinput == "1":
        GetReplies()
        userinput = menu()
    
    #Option 2 - generate images
    # ═══════════════════════════════════════════ 
    elif userinput == "2":
        SaveImages()
        userinput = menu()
    
    # Option 3 - Send images
    # ═══════════════════════════════════════════ 
    elif userinput == "3":
        SendImages()
        userinput = menu()
    
    # Option 4 - Settings
    # ═══════════════════════════════════════════ 
    elif userinput == "4":
        Settings()
        userinput = menu()
    
    # All other options - Repeat menu
    # ═══════════════════════════════════════════ 
    else:     
        PrintBox("Invalid option selected",40)
        userinput = menu()



PrintBox("Program exiting",40)