import os

# Check Folders ===============================================================
up = os.path.expandvars("%USERPROFILE%")
sf = os.path.expandvars("\\Documents\\Sorted Files")
dtop = os.path.expandvars(up + "\\Desktop")
dwn = os.path.expandvars(up + "\\Downloads")
audio = (up + sf + "\\Audio")
fp = (up + sf + "\\Finale Projects")
mp3 = (up + sf + "\\MP3")
mp3 = (up + sf + "\\MP3")
extension = ""
moved_files = 0

# Sorted Files exists?
exist = os.path.isdir(up + sf)
if exist == False:
    os.mkdir(up + sf)

# Sort Desktop Files ==========================================================


for file in os.listdir(dtop):
    if file.find(".") != -1:
        extension = file.split(".")
        extension = extension[-1]
        if extension != "ini":
            exist = os.path.isdir(up + sf + "\\" + extension)
            if exist == False:
                os.mkdir(up + sf + "\\" + extension)
            os.rename(dtop + "\\" + file, up + sf + "\\" + extension + "\\" + file)
            print("Moved \"" + file + "\"")
            moved_files += 1
    else:
        print("Folder \"" + file + "\" Detected")
        
# Sort Downloads Files ========================================================

for file in os.listdir(dwn):
    if file.find(".") != -1:
        extension = file.split(".")
        extension = extension[-1]
        if extension != "ini":
            exist = os.path.isdir(up + sf + "\\" + extension)
            if exist == False:
                os.mkdir(up + sf + "\\" + extension)
            os.rename(dwn + "\\" + file, up + sf + "\\" + extension + "\\" + file)
            print("Moved \"" + file + "\"")
            moved_files += 1
    else:
        print("Folder \"" + file + "\" Detected")

# Results
if moved_files > 1 or moved_files ==0:
    print("\n", moved_files, "Files Moved")
elif moved_files == 1:
    print("\n", moved_files, "File Moved")
input("")
