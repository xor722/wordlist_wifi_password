import subprocess
from pyfiglet import Figlet
import colorama

colorama.init()
f = Figlet(font='big')

output_file = 'wifi_passwords.txt'
with open(output_file, 'w') as f_out:
    # Menampilkan dan menyimpan teks awal
    header_text = colorama.Fore.GREEN + f.renderText('xor 722')
    print(header_text)
    f_out.write(header_text + "\n")

    # Mengambil daftar profil Wi-Fi
    profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')[1:]
    profile_names = [i.split(':')[1][1:-1] for i in profiles if "All User Profile" in i]

    f_out.write("{:<30}| {:<}\n".format("Wi-Fi Name", "Password"))
    f_out.write("-----------------------------------------------\n")

    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    print("-----------------------------------------------")

    for name in profile_names:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            password = [line.split(':')[1][1:-1] for line in results if "Key Content" in line][0]

            output_line = "{:<30}| {:<}".format(name, password)
            print(output_line)
            f_out.write(output_line + "\n")

        except Exception as e:
            output_line = "{:<30}| {:<}".format(name, "Not Found")
            print(output_line)
            f_out.write(output_line + "\n")
