import subprocess

x = subprocess.check_output(['ipconfig']).decode('utf-8')

print(x)

input("Press ENTER to close:")
