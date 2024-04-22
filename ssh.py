#! /usr/bin/python

################################################
#  ssh manager                                 #
# This first module confmanager, who is        #
# responsible for ssh-server.                  #
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
    ssh_manager_art = colored(text2art("ssh manager"), 'yellow')
    ssh_choose = colored('Choose option:', 'yellow')
    ssh_button_1 = colored("1. Enable ssh server",'green')
    ssh_button_2 = colored("2. Disable ssh server",'green')
    ssh_button_3  = colored("3. Install ssh server",'green')
    ssh_configure = colored("4. Configure",'green')
    ssh_back = colored("5. Main menu",'green')
    cprint(f"""{ssh_manager_art}
            {ssh_choose}          
                {ssh_button_1}
                {ssh_button_2}
                {ssh_button_3}
                {ssh_configure}
                {ssh_back}
    


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
            sshconf()
        elif com == '5':
            clear()
            confmanager.main()
        else:
            choose()
def setipport():
    clear()
    ssh_confugure_setipport = colored(text2art('ipv4&port') ,'yellow')
    com = colored('Enter ipv4 address:',"yellow")
    print(f"""
        {ssh_confugure_setipport} 
        {com}    
    """)
    ip = int(input(colored('>',"green")))
    port = input(colored('>',"green"))
    os.system(f"sed -i 14s/")  
    sshconf()

def sshconf():
    clear()
    ssh_configure_art = colored(text2art("configure") ,'yellow')
    ssh_configure_choose = colored('Choose option:','yellow')
    ssh_configure_button_1 = colored("1. Set ip:port" ,"green")
    ssh_configure_button_2 = colored( "2. Enable/Disable passwdauth","green")
    ssh_configure_back = colored("3. Main menu","green")
    print(f"""
        {ssh_configure_art}
            {ssh_configure_choose}
                {ssh_configure_button_1}
                {ssh_configure_button_2}
                {ssh_configure_back}





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
            sshconf()
def main():
    choose()
if __name__ == '__main__':
    main()
