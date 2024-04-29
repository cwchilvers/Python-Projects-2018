import os, shutil


def move_file(item, place):
    if item.endswith(".docx"):
        shutil.move(place + item, folder_docx)
    elif item.endswith(".jpeg") or item.endswith(".jpg"):
        shutil.move(place + item, folder_jpeg)
    elif item.endswith(".mp3"):
        shutil.move(place + item, folder_mp3)
    elif item.endswith(".mp4"):
        shutil.move(place + item, folder_mp4)
    elif item.endswith(".pdf"):
        shutil.move(place + item, folder_pdf)
    elif item.endswith(".png"):
        shutil.move(place + item, folder_png)
    elif item.endswith(".py") or item.endswith(".pyw"):
        shutil.move(place + item, folder_python)
    elif item.endswith(".txt"):
        shutil.move(place + item, folder_txt)
    elif item.endswith(".wav"):
        shutil.move(place + item, folder_wav)
    elif item.endswith(".zip"):
        shutil.move(place + item, folder_zip)
    elif item.endswith(".musx"):
        shutil.move(place + item, folder_finale)
    elif item.endswith(".pptx"):
        shutil.move(place + item, folder_pptx)
    elif item.endswith(".mid"):
        shutil.move(place + item, folder_mid)

desktop = os.path.expandvars("%USERPROFILE%\\Desktop\\")
documents = os.path.expandvars("%USERPROFILE%\\Documents\\")
downloads = os.path.expandvars("%USERPROFILE%\\Downloads\\")
main = os.path.expandvars("%USERPROFILE%\\Documents\\Sort Through\\")
folder_docx = os.path.expandvars(main + "docx\\")
folder_jpeg = os.path.expandvars(main + "jpeg\\")
folder_mp3 = os.path.expandvars(main + "mp3\\")
folder_mp4 = os.path.expandvars(main + "mp4\\")
folder_pdf = os.path.expandvars(main + "pdf\\")
folder_png = os.path.expandvars(main + "png\\")
folder_python = os.path.expandvars(main + "python\\")
folder_txt = os.path.expandvars(main + "txt\\")
folder_wav = os.path.expandvars(main + "wav\\")
folder_zip = os.path.expandvars(main + "zip\\")
folder_finale = os.path.expandvars(main + "finale\\")
folder_pptx = os.path.expandvars(main + "pptx\\")
folder_mid = os.path.expandvars(main + "midi\\")


items = os.listdir(desktop)
place = desktop
for item in items:
    move_file(item, place)


os.chdir(documents)
place = documents
items = os.listdir(documents)
for item in items:
    move_file(item, place)


os.chdir(downloads)
place = downloads
items = os.listdir(downloads)
for item in items:
    move_file(item, place)

    
