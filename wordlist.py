import subprocess
from pyfiglet import Figlet
import colorama

colorama.init()
f = Figlet(font='big')
print(colorama.Fore.GREEN + f.renderText('xor 722'))

profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')[1:]

profile_names = [i.split(':')[1][1:-1] for i in profiles if "All User Profile" in i]

print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("-----------------------------------------------")

for name in profile_names:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        password = [line.split(':')[1][1:-1] for line in results if "Key Content" in line][0]

        print("{:<30}| {:<}".format(name, password))

    except:
        print("{:<30}| {:<}".format(name, "Not Found")) 