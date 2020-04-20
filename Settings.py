import json
from PrintTools import PrintSetting

# Edit Settings
# ═══════════════════════════════════════════ 
def Settings():
    with open('config.json', "r") as f:
        config = json.load(f)

    for key in ["Name","TweetID","FontName","FontSize","FontColor","TextVPosition"]:
        TEMP = PrintSetting(key,config)
        if TEMP != "":
            config[key] = TEMP

    with open('config.json', 'w') as outfile:
        json.dump(config, outfile, indent=4)