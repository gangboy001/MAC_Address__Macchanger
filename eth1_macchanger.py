#!/usr/bin/env python

import os

print("   ____ _                            ")
print("  / ___| |__   __ _ _ __   __ _  ___ ")
print(" | |   | '_ \ / _` | '_ \ / _` |/ _ ")
print(" | |___| | | | (_| | | | | (_| |  __/")
print("  \____|_| |_|\__,_|_| |_|\__, |\___|")
print("  |  \/  | __ _  ___      |___/      ")
print("  | |\/| |/ _` |/ __|                ")
print("  | |  | | (_| | (__                 ")
print("  |_|  |_|\__,_|\___|                ")
print("     _       _     _                 ")
print("    / \   __| | __| |_ __ ___  ___   ")
print("   / _ \ / _` |/ _` | '__/ _ \/ __|  ")
print("  / ___ \ (_| | (_| | | |  __/\__ \  ")
print(" /_/   \_\__,_|\__,_|_|  \___||___/  ")



print("""
Welcome To The Change MAC Address Tool  :)



1) 'eth1' Set MAC Address Random
2) 'eth1' Set MAC Address Manually
3) 'eth1' Reset To Original, Premanent Hardware Mac

""")

processno = raw_input("Please Press The Process Number")
 
                                    
if(processno=="1"):
	os.system("ifconfig eth1 down")
	os.system("macchanger -r eth1")
	os.system("ifconfig eth1 up")
	print("\033[92mThe New MAC Address Was Determined Manually.")

elif(processno=="2"):
	macadres = raw_input("Enter New MAC Address")
	os.system("ifconfig eth1 down")
	os.system("macchanger --mac " + macadres + " eth1")
	os.system("ifconfig eth1 up")
	print("\033[92mThe New MAC Address Was Determined Manually.")

elif(processno=="3"):
	os.system("ifconfig eth1 down")
	os.system("macchanger -p eth1")
	os.system("ifconfig eth1 up")
	print("\033[92mYour Original MAC Address Reset.")

else:
	print("\033[91mYou Click Wrong Button. \033[94mPlease Try Again...")
	os.system("eth1_macchanger.py")




























                                                   


