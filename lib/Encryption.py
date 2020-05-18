import os
from hashlib import *


class Encryption:
    def __init__(self):
        if os.name == "nt":
            os.system("cls")

        elif os.name == "prosix":
            os.system("clear")
        else:
            os.system("cls || clear")

        BANNER = ("""\033[1;31m

   ▄████████  ▄█         ▄▄▄▄███▄▄▄▄    ▄█     ▄████████    ▄████████    ▄████████     ███      ▄█  
  ███    ███ ███       ▄██▀▀▀███▀▀▀██▄ ███    ███    ███   ███    ███   ███    ███ ▀█████████▄ ███  
  ███    ███ ███       ███   ███   ███ ███▌   ███    █▀    ███    ███   ███    ███    ▀███▀▀██ ███▌ \033[1;31m███████████████\033[1;31m
  ███    ███ ███       ███   ███   ███ ███▌   ███         ▄███▄▄▄▄██▀   ███    ███     ███   ▀ ███▌ \033[0;30m███████████████\033[1;31m
▀███████████ ███       ███   ███   ███ ███▌ ▀███████████ ▀▀███▀▀▀▀▀   ▀███████████     ███     ███▌ \033[0;32m███████████████\033[1;31m
  ███    ███ ███       ███   ███   ███ ███           ███ ▀███████████   ███    ███     ███     ███  
  ███    ███ ███▌    ▄ ███   ███   ███ ███     ▄█    ███   ███    ███   ███    ███     ███     ███  
  ███    █▀  █████▄▄██  ▀█   ███   █▀  █▀    ▄████████▀    ███    ███   ███    █▀     ▄████▀   █▀   
             ▀                                             ███    ███
        \033[0m""")
        print(BANNER)
        print("\033[1;32m######## [ Encryption Type ] ######## \033[0m")
        Fuck = ("""\033[1;33m
  1. MD5
  2. SHA1
  3. SHA224
  4. SHA256
  5. SHA384
  6. SHA512
  7. SHA3_224
  8. SHA3_256
  9. SHA3_512
  10. SHA3_384
  11. Blake2b
  12. Blake2s
        \033[0m""")
        print(Fuck)



    def MD5(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = md5(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mMD5\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA1(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha1(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA1\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA224(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha224(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA224\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA256(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha256(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA256\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA384(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha384(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA384\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA512(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha512(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA512\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA3_224(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha3_224(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA3_224\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA3_256(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha3_256(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA3_256\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA3_512(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha3_512(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA3_512\033[1;35m ] \033[0m")
        print("----------------------------------")


    def SHA3_384(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = sha3_384(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mSHA3_384\033[1;35m ] \033[0m")
        print("----------------------------------")


    def Blake2b(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = blake2b(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mBlake2b\033[1;35m ] \033[0m")
        print("----------------------------------")


    def Blake2s(self):
        Hash = input(" \033[1;31m > Enter The Text To Encode : \033[0m ")
        Hash.encode("utf-8")
        Hash = blake2s(Hash.encode()).hexdigest()
        print("\033[1;33m  > Your Hash :\033[0m \033[1;32m",Hash)
        print("\033[0m")
        print("\033[1;35m  > Type : [ \033[1;33mBlake2s\033[1;35m ] \033[0m")
        print("----------------------------------")
