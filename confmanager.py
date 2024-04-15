#! /usr/bin/python
######################################
# This is main file confmanager,
# In this file only cli interface,
# any modules in directory
# Github: 
# Coded by: Vicoder32
######################################
from art import text2art
import os
import sys
from termcolor import colored
import ssh 
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


def menu():
    clear()
    title = colored(text2art('conf manager'), 'yellow')
    co = colored("Choose options:", 'yellow')
    f = colored("1. SSH", 'green')
    s = colored("2. FTP " ,"green")
    t = colored("3. RDP " ,"green")
    fr = colored("4. Apache " ,"green")
    ex = colored("5. Exit", 'green')
    print(f""" {title}     {co}
                    {f}
                    {s}
                    {t}
                    {fr}
                    {ex}
    """)  
    com = colored(input(">"), "green")
    while True:
        if com == '1':
            clear()
            ssh.main()
        elif com == '2':
            pass
        elif com == '3':
            pass
        elif com == '4':
            pass
        elif com == '5':
            clear()
            sys.exit()
        else:
            menu()
def main():
    menu()
if __name__ == '__main__':
    main()
