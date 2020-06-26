from SaveImages import SaveImages
from SendImages import *
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
    userinput = "0"
elif not checkConfig():
        PrintBox("Empty field detected, please edit config.json")
        userinput = "0"
else:
    # diaplay intial menu
    userinput = menu()


while userinput != "0":
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

    # Option 5 - Mark rendered image complete
    # ═══════════════════════════════════════════ 
    elif userinput == "5":
        ViewRenderedImages()
        userinput = menu()
    
    # Option 6 - Mark rendered image complete
    # ═══════════════════════════════════════════ 
    elif userinput == "6":
        ArchiveRenderedImage()
        userinput = menu()
    
    # All other options - Repeat menu
    # ═══════════════════════════════════════════ 
    else:     
        PrintBox("Invalid option selected",40)
        userinput = menu()



PrintBox("Program exiting",40)