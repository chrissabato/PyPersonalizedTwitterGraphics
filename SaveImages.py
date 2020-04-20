from csv import DictReader
from PIL import Image, ImageDraw, ImageFont
import json
from PrintTools import PrintBox

def SaveImages(filename='newfiles.txt'):

    PrintBox("Saving Images")

    with open(filename, 'r') as read_obj:
        dict_reader = DictReader(read_obj)
        replies = list(dict_reader)

    with open('config.json', "r") as f:
        config = json.load(f)

    for reply in replies:

        NAME = reply["name"]
        NUMBER = reply["number"]

        print("  " + NUMBER.rjust(2) + " "+ NAME)

        img = Image.open("default-image.png")
        draw = ImageDraw.Draw(img)

        # Add Name
        FONT = ImageFont.truetype(config["FontName"],config["FontSize"])
        w, h = draw.textsize(NAME.upper(),FONT)
        xpos = (750-w)/2
        draw.text(xy=(xpos,config["TextVPosition"]),text=NAME.upper(),fill=config["FontColor"],font=FONT )

        # Add Number
        numberImg = Image.open("Numbers/" + NUMBER + ".png")
        img.paste(numberImg,(0,0),numberImg)

        img.save("Files/JPEG/"+reply["filename"]+".png","PNG")
    
if __name__ == "__main__":
    SaveImages()