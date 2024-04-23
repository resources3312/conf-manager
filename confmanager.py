#! /usr/bin/python
######################################
# This main file confmanager,
# In this file only cli interface,
# any modules in directory 
# Coded by: Vicoder32
######################################
from art import text2art
import os
import sys
from termcolor import colored
import ssh 
import ftp
import rdp
import apache
def check_root():
    if os.getuid() != 0:
        sys.exit("Running util for root")
    
    else:
        pass


def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system("clear")


def art():
    clear()
    confmanager_art = colored(text2art('confmanager'), 'yellow')
    confmanager_choose = colored("Choose options:", 'yellow')
    confmanager_button_1 = colored("1. SSH", 'green')
    confmanager_button_2 = colored("2. FTP " ,"green")
    confmanager_button_3 = colored("3. RDP " ,"green")
    confmanager_button_4 = colored("4. Apache " ,"green")
    confmanager_exit = colored("5. Exit", 'green')
    print(f""" {confmanager_art}     
                    {confmanager_choose}
                        {confmanager_button_1}
                        {confmanager_button_2}
                        {confmanager_button_3}
                        {confmanager_button_4}
                        {confmanager_exit}
    
 """)  

def menu():
    art()
    com = None
    com = input(colored(">","green"))
    while True:
        if com == "1":
            ssh.main()
        
        elif com == '2':
            ftp.main()
        elif com == '3':
            rdp.main()
        elif com == '4':
            apache.main()       
        elif com == '5':
            sys.exit("Quitting...")
        else:
            menu()
def main():
    menu()
if __name__ == '__main__':
    main()
