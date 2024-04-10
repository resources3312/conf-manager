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

def check_root():
    if os.getuid() != 0:
        sys.exit("Running util for root")
    
    else:
        pass





def menu():
    title = colored(text2art('conf manager'), 'yellow')
    desc = colored("System administration utility", "yellow")
    co = colored("Choose options:", 'yellow')
    f = colored("1. SSH-server", 'green')
    print(f""" {title}
      {desc}
                    {co}
                        {f}


    """)  
    

def main():
    check_root()
    menu()
if __name__ == '__main__':
    main()
