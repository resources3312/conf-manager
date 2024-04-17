#! /usr/bin/python

################################################
#  FTP manager                                 #
# This second module confmanager, who is       #
# responsible for ssh-server. I fell lik=e     #
#  Linus Torvalds, which write descriptions    #
#                                              #
#  Github:                                     #
#  Coded by: ViCoder32                         #
#                                              #
################################################

import socket
import os
import sys
from art import text2art
from termcolor import colored
import confmanager
global ip

def check_root():
    if os.getuid() != 0:
        sys.exit("Running script with root")
    else:
        pass



def get_local_ipv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()


def main():
    check_root()

if __name__ == '__main__':
    main()
