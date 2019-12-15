import sys
from PIL import Image
from termcolor import colored

def hide_text(img_file, msg):
    img = Image.open(img_file)
    length = len(msg)
    # use a copy of image to hide the text in
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            # first value is length of msg
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))
            index += 1
    encoded.save("encoded.png")
    
def clear_text(img_file):
    img = Image.open(img_file)
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                # need to add transparency a for some .png files
                r, g, b, a = img.getpixel((col, row))		
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg

if(len(sys.argv) == 3):
    if(sys.argv[1] == "-e"):
        text=input(colored("Enter text to hide in ", "blue")+colored(sys.argv[2], "yellow")+ " :> ")
        hide_text(sys.argv[2], text)
        print(colored("The image saved in ", "blue")+colored("encoded.png", "yellow"))
    elif(sys.argv[1] == "-d"):
        text=clear_text(sys.argv[2])
        print(colored("Text found in ", "blue"), colored(sys.argv[2], "yellow"))
        print(colored(text, "green"))
else:
    print(colored("python stechnography.py -e 'images.png'\npython stechnography.py -d 'images.png'", "blue"))
