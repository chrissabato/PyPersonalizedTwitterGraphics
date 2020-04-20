def GetReplies():
    import csv, tweepy, json, os 
    import os.path
    from os import path
    from PrintTools import PrintBox

    #get list of tweets that have been replied to or marked to ignore
    with open('replied.txt', 'r') as f:
        replied = f.read().splitlines()


    # load credentials
    with open('config.json', "r") as f:
        config = json.load(f) 
    auth = tweepy.OAuthHandler(config["APIKey"], config["APISecret"])
    auth.set_access_token(config["AccessToken"], config["AccessTokenSecret"])

    api = tweepy.API(auth)

    # function to verify tweet contents
    # ═══════════════════════════════════════════ 
    def verifyRequest(tweet,correctedTweet=""):

        if correctedTweet == "":
            usertext = tweet.text.replace('@'+config["Name"]+' ', '').split(',')
        elif correctedTweet == "-i":
            replied.append(tweet.id)
            with open('replied.txt', 'a',) as f:
                f.write(str(tweet.id)+"\n")
            return False
        else:
            usertext = correctedTweet.split(',')
            
        usertext = [item.strip() for item in usertext]

        if str(tweet.id) not in replied:   
            if len(usertext)==2 and usertext[0].isdigit():   
                filename = tweet.user.screen_name + "-"+str(tweet.id)
                return {'filename': filename, 'number': usertext[0],'name':usertext[1]}
                
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("╔═══════════════════════════════════════════╗")
                print("║ Enter to skip | -i to ignore permanently  ║")
                print("║ Use format: Number,Name to correct        ║")
                print("╠═════════╦═════════════════════════════════╣")
                print("║ REQUEST ║ " + tweet.text.replace('@'+config["Name"]+' ', '').ljust(32) + "║")
                print("╚═════════╩═════════════════════════════════╝")
                userinput = input()
                if userinput == "":
                    return False
                else:
                    return verifyRequest(tweet,userinput)
        else:
            return False


    # Save All replies
    # ═══════════════════════════════════════════ 
    replies=[]
    for tweet in tweepy.Cursor(api.search,q='to:'+config["Name"], result_type='recent', timeout=999999).items(1000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==config["TweetID"]):
                replies.append(tweet)


    count=0
    with open('newfiles.txt', 'w',newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['filename','number','name'])
        writer.writeheader()
        for tweet in replies:
            row = verifyRequest(tweet)
            if row:
                writer.writerow(row)
                count += 1

    tmp = str(count).rjust(3,"0") + " new requests"
    PrintBox(tmp)

    return count
