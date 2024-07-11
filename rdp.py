#! /usr/bin/python

################################################
#  rdp manager                                 #
# This first module confmanager, who is        #
# responsible for rdp-server. I fell like      #
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
        return ip
    except:
           print("Connect for network and try again ")

def definedistr():
    f = open('/etc/os-release', 'r')
    raw = f.read()
    data = raw.split()
    distr = data[9].split('=')[1]
    f.close()
    if distr != None:
        return distr
    else:
        return False



def rdpinstall():
    os.system("apt update")
    os.system("apt install xrdp -y")
    os.system("apt install xorgrdp -y")
    clear()
    menu()
def rdpdown():
    if sys.platform == 'win*':
        pass
    else:
         os.system("systemctl disable xrdp")
         clear()
    menu()
def rdpup():
    if sys.platform == 'win*':
        pass

    else:
         os.system("systemctl enable xrdp")
         os.system("systemctl restart xrdp")
    clear()
    menu()
def menu():
    clear()
    rdp_manager_art = colored(text2art("rdp manager"), 'yellow')
    rdp_manager_menu = colored('Choose option:', 'yellow')
    rdp_manager_button_1 = colored("1. Enable rdp server",'green')
    rdp_manager_button_2 = colored("2. Disable rdp server",'green')
    rdp_manager_button_3 = colored("3. Install rdp server",'green')

    rdp_manager_button_4 = colored("4. Configure",'green')
    rdp_manager_back = colored("5. Main menu",'green')
    cprint(f"""{rdp_manager_art}
        
        {rdp_manager_menu}
            {rdp_manager_button_1}
            {rdp_manager_button_2}
            {rdp_manager_button_3}
            {rdp_manager_button_4}
            {rdp_manager_back}
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
            menu()
        elif com == '4':
            rdpconf()
        elif com == '5':
            clear()
            confmanager.main()
        else:
            menu()
def setipport():
    clear()
    rdp_configure_setiport_art = colored(text2art('ipv4&port') ,'yellow')
    rdp_configure_button_1 = colored('Enter ipv4 address:',"yellow")
    print(f"""
        {rdp_configure_setiport_art} 
        
    {rdp_configure_button_1}    

""")
    ip = 'Port' + int(input(colored('>',"green")))
    port = input(colored('>',"green"))
    os.system(f"sed -i 14s/")     
    rdpconf()

def rdpconf():
    clear()
    rdp_configure_art = colored(text2art("configure") ,'yellow')
    rdp_configure_menu = colored('Choose option:','yellow')
    rdp_configure_button_1 = colored("1. Set ip:port" ,"green")
    rdp_configure_button_2 = colored( "2. Enable/Disable passwdauth","green")
    rdp_configure_back = colored("3. Main menu","green")
    print(f"""
        {rdp_configure_art}
            {rdp_configure_menu}
                {rdp_configure_button_1}
                {rdp_configure_button_2}
                {rdp_configure_back}

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
            rdpconf()
def main():
    menu()
if __name__ == '__main__':
    main()
