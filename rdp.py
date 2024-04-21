#! /usr/bin/python

################################################
#  ssh manager                                 #
# This first module confmanager, who is        #
# responsible for ssh-server. I fell like      #
#  Linus Torvalds, which write descriptions    #
#  for Linux sources = >                       #
#  Github:                                     #
#  Coded by: ViCoder32                         #
#                                              #
################################################

import socket
import os
import sys
from art import text2art
from termcolor import colored, cprint
import confmanager
global ip
def check_root():
    if os.getuid() != 0:
        sys.exit("Running script with root")
    else:
        pass



def clear():
    if sys.platform == 'win32':
        os.system("cls")
    else:
        os.system("clear")
def get_local_ipv4():
    try:    
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except:
           print("Connect for network and try again ")
def rdpinstall():
    os.system("apt update")
    os.system("apt install openssh-server -y")
    clear()
    choose()
def rdpdown():
    if sys.platform == 'win*':
        pass
    else:
         os.system("systemctl disable ssh")
         clear()
    choose()
def rdpup():
    if sys.platform == 'win*':
        pass

    else:
         os.system("systemctl enable ssh")
         os.system("systemctl restart ssh")
    clear()
    choose()
def choose():
    clear()
    a = colored(text2art("rdp manager"), 'yellow')
    op = colored('Choose option:', 'yellow')
    b = colored("1. Enable rdp server",'green')
    t = colored("2. Disable rdp server",'green')
        
    d = colored("3. Install rdp server",'green')

    con = colored("4. Configure",'green')
    ex = colored("5. Main menu",'green')
    cprint(f"""{a}
        
        {op}
            {b}
            {t}
            {d}
            {con}
            {ex}
    """, 'yellow')
    com = ''
    com = input(colored('>', 'green'))
    while True:
        if com == '1':
            clear()
            rdppup()
        elif com == '2':
            clear()
            rdpdown()
        elif com == '3':
            clear()
            rdpinstall()
            choose()
        elif com == '4':
            rdpconf()
        elif com == '5':
            clear()
            confmanager.main()
        else:
            choose()
def setipport():
    clear()
    ar = colored(text2art('ipv4&port') ,'yellow')
    en = colored('Enter ipv4 address:',"yellow")
    print(f"""
        {ar} 
        
    {en}    




    """)
    ip = 'Port' + int(input(colored('>',"green")))
    port = input(colored('>',"green"))
    os.system(f"sed -i 14s/")  # 14, 16, 57 strings this main part conffile
    sshconf()

def rdpconf():
    clear()
    confart = colored(text2art("configure") ,'yellow')
    coc = colored('Choose option:','yellow')
    fo = colored("1. Set ip:port" ,"green")
    so = colored( "2. Enable/Disable passwdauth","green")
    to = colored("3. Main menu","green")
    print(f"""
        {confart}
            {coc}
                {fo}
                {so}
                {to}





    """)
    ent = ''
    ent = input(colored('>' ,"green"))
    while True:
        if ent == '1':
            setipport()
        elif ent == '2':
            pass
            #passwdauth()
        elif ent == '3':
            main()
        else:
            rdpconf()
def main():
    choose()
if __name__ == '__main__':
    main()
