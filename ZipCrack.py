# Owner : ☠︎︎⚠︎🇷 🇦 🇻 🇦 🇳⚠︎ ☠︎︎ 
# Version : 1.5
# Build Date : 22/12/2024
# Instagram : itz_ravan_07__

# Import required modules
import os
import time

# Writer function to display text with animation
def writer(text):
    for x in text:
        print(x, end='', flush=True)
        time.sleep(0.04)
    print()

# Import necessary modules and handle missing modules
try:
    import pyzipper
    import itertools
    import string
    from colorama import init
except ImportError:
    writer('Installing required modules...')
    os.system("pip install pyzipper")
    os.system("pip install colorama")
    os.system("clear")
    import pyzipper
    from colorama import init

# Initialize colorama
init()
os.system("clear")
#urls
y_url ="https://youtube.com/@hackers_colony_tech?si=Dy6hDgWH5rnONP9a"
i_url="https://www.instagram.com/hackers_colony_official?igsh=Ym42ZnVnY3JjbHp0"
w_url="https://chat.whatsapp.com/Ha3goS71RamKMeCq2CJLwe"

# Display welcome banner and information
hading = '''
\033[32m
                                                                                                              
    _/    _/    _/_/_/    _/_/                  _/                                                    _/      
   _/    _/  _/        _/    _/      _/_/_/_/      _/_/_/      _/_/_/  _/  _/_/    _/_/_/    _/_/_/  _/  _/   
  _/_/_/_/  _/        _/    _/          _/    _/  _/    _/  _/        _/_/      _/    _/  _/        _/_/      
 _/    _/  _/        _/    _/        _/      _/  _/    _/  _/        _/        _/    _/  _/        _/  _/     
_/    _/    _/_/_/    _/_/        _/_/_/_/  _/  _/_/_/      _/_/_/  _/          _/_/_/    _/_/_/  _/    _/    
                                               _/                                                             
                                              _/    _/_/_/_/_/                                                
'''

writer(hading)
writer("""\033[1;4;35;47m✨ **Welcome to Hackers Colony ZIP Cracker!** ✨\033[0m

\033[34m### 🔥 Tool Name:\033[0m\033[1;31;42m Hackers Colony Zip_Cracker 🔥
\033[1;4;37m
This tool uses brute-force methods to crack ZIP file passwords. Provide the file path, and the tool will attempt to find the password systematically.
\033[0m
""")

#opening links function
time.sleep(2)
writer("\033[31mOening YouTube")
os.system(f"termux-open {y_url}")
time.sleep(6)
writer("Type 'Enter' to next stap: ")
input()
writer("\033[35mOening Instagram")
os.system(f"termux-open {i_url}")
time.sleep(6)
writer("Type 'Enter' to next stap: ")
input()
writer("\033[32mOening WhatsApp")
os.system(f"termux-open {w_url}")
time.sleep(7)
print('\n' * 3)

# Function to brute-force ZIP file passwords
def crack_zip(zip_file, min_length, max_length):
    # Character set for password combinations
    characters = string.ascii_letters + string.digits + string.punctuation

    # Check if file exists
    if not os.path.isfile(zip_file):
        writer("\033[31mError: File not found!")
        return False

    # Attempt password cracking
    with pyzipper.AESZipFile(zip_file) as zf:
        for length in range(min_length, max_length + 1):
            writer(f"\033[34mCurrently testing passwords of length {length}...\033[0m")
            for password in itertools.product(characters, repeat=length):
                password = ''.join(password)
                print(f'\033[32mTrying\033[31m {password}\033[0m')
                try:
                    zf.extractall(pwd=password.encode('utf-8'))
                    writer(f"\033[1;33mPassword found:\033[1;32m {password}")
                    with open("log.txt", 'a') as f:
                        f.write(f"{zip_file} : {password}\n")
                    return True
                except (RuntimeError, pyzipper.BadZipFile):
                    continue
    writer("\033[1;37mPassword could not be cracked...")
    return False

# Get user input
writer("\033[32mEnter the ZIP file name (e.g., test.zip): ")
zip_file_path = input()
writer("\033[35mEnter minimum password length (default 0): ")
min_password_length = int(input() or "0")
writer("\033[33mEnter maximum password length (default 8): ")
max_password_length = int(input() or "8")

# Start brute-forcing
crack_zip(zip_file_path, min_password_length, max_password_length)