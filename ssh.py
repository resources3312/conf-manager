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
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
def sshinstall():
    os.system("apt update")
    os.system("apt install openssh-server -y")
    clear()
    choose()
def sshdown():
    if sys.platform == 'win*':
        pass
    else:
         os.system("systemctl disable ssh")
         clear()
    choose()
def sshup():
    if sys.platform == 'win*':
        pass

    else:
         os.system("systemctl enable ssh")
         os.system("systemctl restart ssh")
    clear()
    choose()
def choose():
    clear()
    a = colored(text2art("ssh manager"), 'yellow')
    op = colored('Choose option:', 'yellow')
    b = colored("1. Enable ssh server",'green')
    t = colored("2. Disable ssh server",'green')
        
    d = colored("3. Install ssh server",'green')
    e = colored("4. Main menu", 'green')

    cprint(f"""{a}
        
        {op}
            {b}
            {t}
            {d}
            {e}
    """, 'yellow')
    com = ''
    com = input(colored('>', 'green'))
    while True:
        if com == '1':
            clear()
            sshup()
        elif com == '2':
            clear()
            sshdown()
        elif com == '3':
            clear()
            sshinstall()
            choose()
        elif com == '4':
            clear()
            confmanager.main()
        else:
            choose()
def main():
    choose()
if __name__ == '__main__':
    main()
