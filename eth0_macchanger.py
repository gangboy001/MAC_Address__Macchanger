#!/usr/bin/env python

import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MACCHANGER BY IT-WORLD")

print("""
1) 'eth0' Set MAC Address Random
2) 'eth0' Set MAC Address Manually
3) 'eth0' Reset TO Original, Premanent MAC

""")

processno = raw_input("Please Press The Proccess Number: ")

if(processno=="1"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mThe New MAC Adress Was Determined Manually.")

elif(processno=="2"):
    macadres = raw_input("Enter New MAC Address")
    os.system("ifconfig eth0 down")
    os.system("macchanger --m " + macadres + " eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mThe New MAC Adress Was Determined Manually.")

elif(processno=="3"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -p eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mYour Origiinal MAC Address Reset.")

else:
    print("\033[91mYou Click Wrong Button. \033[94mPlease Try Again...")
    os.system("eth0_macchanger")