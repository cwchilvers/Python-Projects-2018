from pytube import YouTube
import os

mode = 1
choice = ""

def convert():
    destination = os.path.expandvars("%userprofile%/Downloads")
    link = input("Enter video address:\n")
    try:
        YouTube(link).streams.first().download(destination)
        print("\nDone. \n\n\"" + YouTube(link).title + "\" \n...has been saved to your downloads folder.\n")
    except Exception as error:
        print("\nERROR")
        print(str(error) + "\n")

def again():
    again = input("Download another video? (Y/N)\n")
    if again.upper () == "Y" or again.upper () == "YES":
        x = 1 
    elif again.upper () != "Y" or again.upper () != "YES":
        if again.upper() == "N" or again.upper() == "NO":
            x = 0
        else:
            x = 2
    return(x)

def new_screen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

new_screen()
convert()
while mode == 1:
    choice = again()
    if choice == 1:
        new_screen()
        convert()
    if choice == 2:
        again()
    if choice == 0:
        break
