import socket
import sys
import os

os.system("clear")
#color
W = '\033[1;34;40m'
print(W)

#code
os.system("figlet SIMPLE SCAN")
print(" \033[1;31m  make by 『Clairks✇MT』")
print(W)
hostname = input("Enter website : \033[1;31m")
print(W)
ip = socket.gethostbyname(hostname)
print(" ")                                                            
print("website hostname : \033[1;31m ",hostname) ; print(W)
print("website ip : \033[1;31m ",ip)
print(" ")
print(W)
os.system("nmap --script-updatedb "+ip)
