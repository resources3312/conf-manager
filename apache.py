#! /usr/bin/python
################################################
#  apache manager                                 #
# This first module confmanager, who is        #
# responsible for ssh-server.                  #
# Coded by: ViCoder32                          #
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

def definedistr():
    with open('/etc/os-release', 'r') as f:
        raw = f.read()
        data = raw.split()
        print(data[9].split('=')[1])




def apacheinstall():
    os.system("apt update")
    os.system("apt install openssh-server -y")
    clear()
    choose()
def apachedown():
    if sys.platform == 'win*':
        pass
    else:
         os.system("systemctl disable ssh")
         clear()
    choose()
def apacheup():
    if sys.platform == 'win*':
        pass

    else:
         os.system("systemctl enable ssh")
         os.system("systemctl restart ssh")
    clear()
    choose()
def choose():
    clear()
    apache_manager_art = colored(text2art("apache manager"), 'yellow')
    apache_choose = colored('Choose option:', 'yellow')
    apache_button_1 = colored("1. Enable apache server",'green')
    apache_button_2 = colored("2. Disable apache server",'green')
        
    apache_button_3 = colored("3. Install apache server",'green')

    apache_configure = colored("4. Configure",'green')
    apache_back = colored("5. Main menu",'green')
    cprint(f"""{apache_manager_art}
        
        {apache_choose}
            {apache_button_1}
            {apache_button_2}
            {apache_button_3}
            {apache_configure}
            {apache_back}
    """, 'yellow')
    com = ''
    com = input(colored('>', 'green'))
    while True:
        if com == '1':
            clear()
            apacheup()
        elif com == '2':
            clear()
            apachedown()
        elif com == '3':
            clear()
            apacheinstall()
            choose()
        elif com == '4':
            apacheconf()
        elif com == '5':
            clear()
            confmanager.main()
        else:
            choose()
def setipport():
    clear()
    apache_configure_setipport_art = colored(text2art('ipv4&port') ,'yellow')
    apache_configure_setipport_button_1 = colored('Enter ipv4 address:',"yellow")
    print(f"""
        {apache_configure_setipport_art} 
            {apache_configure_setipport_button_1 }    

""")
    ip = 'Port' + int(input(colored('>',"green")))
    port = input(colored('>',"green"))
    os.system(f"sed -i 14s/")
    sshconf()

def apacheconf():
    clear()
    apache_configure_art = colored(text2art("configure") ,'yellow')
    apache_configure_choose = colored('Choose option:','yellow')
    apache_configure_button_1 = colored("1. Set ip:port" ,"green")
    apache_configure_button_2 = colored( "2. Enable/Disable passwdauth","green")
    apache_configure_button_3 = colored("3. Main menu","green")
    print(f"""
        { apache_configure_art}
            {apache_configure_choose}
                {apache_configure_button_1}
                {apache_configure_button_2}
                {apache_configure_button_3}

""")
    com = ''
    com = input(colored('>' ,"green"))
    while True:
        if com == '1':
            setipport()
        elif com == '2':
            pass
            #passwdauth()
        elif com == '3':
            main()
        else:
            apacheconf()
def main():
    choose()
if __name__ == '__main__':
    main()
