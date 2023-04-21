import hashlib
from concurrent.futures import ThreadPoolExecutor

def hash_password(password):
    with open("10MpassSHA1.txt", "a") as fw:
        fw.write(hashlib.sha1(password.encode()).hexdigest() + ":" + password + "\n")

with open("10Mpass.txt", "r") as fw:
    with ThreadPoolExecutor() as executor:
        for line in fw:
            line = line.strip()
            executor.submit(hash_password, line)