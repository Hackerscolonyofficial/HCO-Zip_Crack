# Owner : ☠︎︎⚠︎🇷 🇦 🇻 🇦 🇳⚠︎ ☠︎︎ 
# version : 1.0
# Build date : 22/12/2024
# instagram : itz_ravan_07__

#import modules
import os
import time

#import modules
try:
    import pyzipper
    import itertools
    import string
    from colorama import init
except:
    writer('Installing module...')
    os.system("pip install pyzipper")
    os.system("pip install colorama")
    os.system("clear")
    import pyzipper
    from colorama import init

init()
os.system("clear")
#urls 
w_url = "https://chat.whatsapp.com/Ha3goS71RamKMeCq2CJLwe"
i_url = "https://www.instagram.com/itz_ravan_07__/profilecard/?igsh=cjA2aDh3Mnd2eXd2"
y_url = "https://youtube.com/@hackers_colony_tech?si=eTff8JBvqRHCFuu1"

#hadings
sub_hading = '''\033[1;31m

 ██░ ██ ▄████▄  ▒█████     ▒███████▒██▓██▓███  ▄████▄  ██▀███  ▄▄▄      ▄████▄  ██ ▄█▀
▓██░ ██▒██▀ ▀█ ▒██▒  ██▒   ▒ ▒ ▒ ▄▀▓██▓██░  ██▒██▀ ▀█ ▓██ ▒ ██▒████▄   ▒██▀ ▀█  ██▄█▒ 
▒██▀▀██▒▓█    ▄▒██░  ██▒   ░ ▒ ▄▀▒░▒██▓██░ ██▓▒▓█    ▄▓██ ░▄█ ▒██  ▀█▄ ▒▓█    ▄▓███▄░ 
░▓█ ░██▒▓▓▄ ▄██▒██   ██░     ▄▀▒   ░██▒██▄█▓▒ ▒▓▓▄ ▄██▒██▀▀█▄ ░██▄▄▄▄██▒▓▓▄ ▄██▓██ █▄ 
░▓█▒░██▒ ▓███▀ ░ ████▓▒░   ▒███████░██▒██▒ ░  ▒ ▓███▀ ░██▓ ▒██▒▓█   ▓██▒ ▓███▀ ▒██▒ █▄
 ▒ ░░▒░░ ░▒ ▒  ░ ▒░▒░▒░    ░▒▒ ▓░▒░░▓ ▒▓▒░ ░  ░ ░▒ ▒  ░ ▒▓ ░▒▓░▒▒   ▓▒█░ ░▒ ▒  ▒ ▒▒ ▓▒
 ▒ ░▒░ ░ ░  ▒    ░ ▒ ▒░    ░░▒ ▒ ░ ▒▒ ░▒ ░      ░  ▒    ░▒ ░ ▒░ ▒   ▒▒ ░ ░  ▒  ░ ░▒ ▒░
 ░  ░░ ░       ░ ░ ░ ▒     ░ ░ ░ ░ ░▒ ░░      ░         ░░   ░  ░   ▒  ░       ░ ░░ ░ 
 ░  ░  ░ ░         ░ ░       ░ ░    ░         ░ ░        ░          ░  ░ ░     ░  ░   
       ░                   ░                  ░                        ░              
'''


hading = '''\033[1;32m
  _    _  _____ ____        _                           _    
 | |  | |/ ____/ __ \      (_)                         | |   
 | |__| | |   | |  | |  _____ _ __   ___ _ __ __ _  ___| | __
 |  __  | |   | |  | | |_  / | '_ \ / __| '__/ _` |/ __| |/ /
 | |  | | |___| |__| |  / /| | |_) | (__| | | (_| | (__|   < 
 |_|  |_|\_____\____/  /___|_| .__/ \___|_|  \__,_|\___|_|\_\
                             | |______                       
                             |_|______|                      
'''

#writer function
def writer(text):
    for x in text:
        print(x, end='', flush=True)
        time.sleep(0.04)
    print()


writer(hading)
writer("""\033[1;4;35;47m✨ **Welcome to the Ultimate Experience!** ✨\033[0m

\033[34m### 🔥 Tool Name:\033[0m\033[1;31;42m Hackers Colony Zip_Cracker 🔥
\033[1;4;37m
We are thrilled to have you here! To unlock the full potential of this amazing tool and become part of our growing community, just follow these simple steps:
\033[0m
\033[1;31m1. ✅ Subscribe to our YouTube channel for exclusive updates, tips, and tutorials.\033[0m
\033[1;34m2. 🌟 Follow us on Instagram to stay connected and enjoy exciting behind-the-scenes content.\033[0m
\033[1;32m3. 🤝 Join our official WhatsApp Group for direct support, updates, and a chance to interact with like-minded users.\033[0m
\033[4;34m
By supporting us, you ensure continuous improvements and future innovations. Thank you for being a part of our journey! 🙌\033[0m""")
print('\n'*3)
time.sleep(5)
writer("\033[31mOpening Youtube....")
os.system(f"termux-open {y_url}")
input("\033[35mType ENTER to Follow insta....")
writer("\033[35mOpening instagram....")
os.system(f"termux-open {i_url}")
input("\033[32mType ENTER to joining group....")
os.system(f"termux-open {w_url}")
time.sleep(5)
os.system('clear')
writer(sub_hading)
print()
writer("-"*200)
print()
writer("""\033[1;32m
How It Works:

1. Provide the full path of the zip file you want to crack.


2. Specify the minimum (default 0) and maximum (default 9999999) password length.


3. The tool will try all possible password combinations within the given length range using brute force.


4. Once the correct password is found, the zip file will be unlocked.\033[0m""")

def crack_zip(zip_file, min_length, max_length):
    characters = string.ascii_letters + string.digits
    with pyzipper.AESZipFile(zip_file) as zf:
        for length in range(min_length, max_length + 1):
            for password in itertools.product(characters, repeat=length):
                password = ''.join(password)
                print(f'\033[32mTrying\033[31m {password}\033[0m')
                try:
                    zf.extractall(pwd=password.encode('utf-8'))
                    writert(f"\033[1;33mPassword is:\033[1;32m {password}")
                    with open("log.txt", 'a') as f:
                        f.write(f"{zip_file} : {password} \n")
                    return True
                except Exception as e:
                    pass
    writer("\033[1;37mPassword not crackable....")
    return False
print("\n"*3)
writer("\033[32mEnter file name endswith(.zip): ")
zip_file_path = input()
writer("\033[35mEnter minimum length(Default 0): ")
min_password_length = int(input()or "0")
writer("\033[33mEnter maximum length(Default 999999): ")
max_password_length = int(input()or "9999999")

crack_zip(zip_file_path,min_password_length, max_password_length)
