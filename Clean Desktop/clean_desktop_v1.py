import os, shutil


def move_file(item):
    if item.endswith(".docx"):
        shutil.move(desktop + item, folder_docx)
    elif item.endswith(".jpeg") or item.endswith(".jpg"):
        shutil.move(desktop + item, folder_jpeg)
    elif item.endswith(".mp3"):
        shutil.move(desktop + item, folder_mp3)
    elif item.endswith(".mp4"):
        shutil.move(desktop + item, folder_mp4)
    elif item.endswith(".pdf"):
        shutil.move(desktop + item, folder_pdf)
    elif item.endswith(".png"):
        shutil.move(desktop + item, folder_png)
    elif item.endswith(".py") or item.endswith(".pyw"):
        shutil.move(desktop + item, folder_python)
    elif item.endswith(".txt"):
        shutil.move(desktop + item, folder_txt)
    elif item.endswith(".wav"):
        shutil.move(desktop + item, folder_wav)
    elif item.endswith(".zip"):
        shutil.move(desktop + item, folder_zip)
    elif item.endswith(".musx"):
        shutil.move(desktop + item, folder_finale)
    elif item.endswith(".pptx"):
        shutil.move(desktop + item, folder_pptx)
    elif item.endswith(".mid"):
        shutil.move(desktop + item, folder_mid)

desktop = os.path.expandvars("%USERPROFILE%\\Desktop\\")
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

for item in items:
    move_file(item)
