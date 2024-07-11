#! /usr/bin/python

################################################
#  ftp manager                                 #
# This first module confmanager, who is        #
# responsible for ssh-server.                  #
# Coded by: ViCoder*                          #
#                                              #
################################################

import socket
import os
import sys
from art import text2art
from termcolor import colored, cprint
import confmanager




def check_root():
    if os.getuid() != 0:
        sys.exit("Running script with root")
    else:
        pass



def clear():
    if sys.platform == 'win*':
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
    with open('/etc/os-release', 'r') as f:
        raw = f.read()
        data = raw.split()
        print(data[9].split('=')[1])


def ftpinstall():
    if sys.platform == 'win*':
        clear()
        try:
         os.system("scoop install <service>")
        except:
            print("scoop not installed")
            os.system("""Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression""")
            clear()
            sshinstall()
    else:
        clear()
        apt = ['debian', 'ubuntu']
        yum = ['centos']
        dnf = ['fedora']
        pacman = ['arch']
        rpm = []
        emerge = ['gentoo']
        distr = definedistr()
        if distr in apt:
            os.system('apt update -y')
            os.system('apt install openssh-server -y')
        elif distr in yum:
            pass
        elif distr in dnf:
            os.system("dnf update")
            os.system('dnf install openssh-server -y')
        elif distr in pacman:
            os.system('pacman -Sy')
            os.system('pacman -S openssh')
        elif distr in rpm:
            os.system("rpm update")
            os.system('rpm install ')
        elif distr in emerge:
            os.system('emerge --sync')
            os.system('emerge openssh')
        else:
            menu()

        menu()


def ftpdown():
    if sys.platform == 'win*':
        pass
    else:
         os.system("systemctl disable ssh")
         clear()
    menu()
def ftpup():
    if sys.platform == 'win*':
        pass

    else:
         os.system("systemctl enable ssh")
         os.system("systemctl restart ssh")
    clear()
    menu()
def menu():
    clear()
    ftp_manager_art = colored(text2art("ftp manager"), 'yellow')
    ftp_menu = colored('Choose option:', 'yellow')
    ftp_button_1 = colored("1. Enable ftp server",'green')
    ftp_button_2 = colored("2. Disable ftp server",'green')
        
    ftp_button_3 = colored("3. Install ftp server",'green')

    ftp_configure = colored("4. Configure",'green')
    ftp_back = colored("5. Main menu",'green')
    cprint(f"""{ftp_manager_art}
        
        {ftp_menu}
            {ftp_button_1}
            {ftp_button_2}
            {ftp_button_3}
            {ftp_configure}
            {ftp_back}
    """, 'yellow')
    com = ''
    com = input(colored('>', 'green'))
    while True:
        if com == '1':
            clear()
            ftpup()
        elif com == '2':
            clear()
            ftpdown()
        elif com == '3':
            clear()
            ftpinstall()
            menu()
        elif com == '4':
            ftpconf()
        elif com == '5':
            clear()
            confmanager.main()
        else:
            menu()
def setipport():
    clear()
    ftp_configure_setipport_art = colored(text2art('ipv4&port') ,'yellow')
    ftp_configure_setipport_button_1 = colored('Enter ipv4 address:',"yellow")
    print(f"""
        {ftp_configure_setipport_art} 
            {ftp_configure_setipport_button_1 }    

""")
    ip = 'Port' + int(input(colored('>',"green")))
    port = input(colored('>',"green"))
    os.system(f"sed -i 14s/")
    sshconf()

def ftpconf():
    clear()
    ftp_configure_art = colored(text2art("configure") ,'yellow')
    ftp_configure_menu = colored('Choose option:','yellow')
    ftp_configure_button_1 = colored("1. Set ip:port" ,"green")
    ftp_configure_button_2 = colored( "2. Enable/Disable passwdauth","green")
    ftp_configure_button_3 = colored("3. Main menu","green")
    print(f"""
        { ftp_configure_art}
            {ftp_configure_menu}
                {ftp_configure_button_1}
                {ftp_configure_button_2}
                {ftp_configure_button_3}

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
            ftpconf()
def main():
    menu()
if __name__ == '__main__':
    main()
