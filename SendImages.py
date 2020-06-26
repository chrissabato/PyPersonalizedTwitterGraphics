import tweepy, json, glob, os, os.path
from PrintTools import PrintBox

def SendImages():

    # get credentials at developer.twitter.com
    with open('config.json', "r") as f:
        config = json.load(f) 
    auth = tweepy.OAuthHandler(config["APIKey"], config["APISecret"])
    auth.set_access_token(config["AccessToken"], config["AccessTokenSecret"])

    api = tweepy.API(auth)

    count = 0
    dirList = os.listdir('Files/JPEG')

    PrintBox("Sending Images")


    for file in dirList:
        fileloc  = 'Files/JPEG/'+file
        
        # Split filename to get Twitter handle and Tweet ID
        tweet = file.replace(".jpg","").replace(".png","").split('-')
        api.update_with_media(filename=fileloc,status = 'Here ya go', in_reply_to_status_id = tweet[1] , auto_populate_reply_metadata=True)
        
        print("Reply sent to @"+tweet[0])
        
        # Add tweet id to sent list
        with open('replied.txt', 'a',) as f:
            f.write(tweet[1]+"\n")
        
        # Delete JPG after reply sent
        os.unlink(fileloc)
        count += 1 

    tmp = str(count).rjust(3,"0") + " files sent"
    PrintBox(tmp)


def ViewRenderedImages():
    dirList = os.listdir('Files/JPEG/')
    print("╔═══════════════════════════════════════════╗")
    for index, file in enumerate(dirList):
        tweet = file.replace(".jpg","").replace(".png","").split('-')
        print("║ "+str(index).rjust(2) + " — @" +tweet[0].ljust(15) +" "+tweet[1] + " ║")
    print("╚═══════════════════════════════════════════╝")
    return dirList

def ArchiveRenderedImage():
    dirList = ViewRenderedImages()
    userinput = input()
    
    if userinput == "":
        return True
    else:
        filename=dirList[int(userinput)]
        PrintBox("Archiving: "+filename)
        fileloc  = "Files/JPEG/"+filename
        os.unlink(fileloc)
        
        # Add tweet id to sent list
        tweet = filename.replace(".jpg","").replace(".png","").split('-')
        with open('replied.txt', 'a',) as f:
            f.write(tweet[1]+"\n")


        ViewRenderedImages()


