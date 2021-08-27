import os
from time import sleep
os.system('cls')

#Importing Colorama
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#Importing main.py 
import main

print(Fore.CYAN+'''
█████████████████████████████████████
█▄─▄▄─█░▄▄░▄█▄─▀█▀─▄██▀▄─██▄─▄█▄─▄███
██─▄█▀██▀▄█▀██─█▄█─███─▀─███─███─██▀█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀''')
print("--------------------------------------")
menu = {}
menu[Fore.LIGHTYELLOW_EX+'[1]']="Send Email to one recipient" 
menu[Fore.LIGHTYELLOW_EX+'[2]']="Send Email to multiple recipient"
menu[Fore.LIGHTYELLOW_EX+'[3]']="Check the recipients"
menu[Fore.LIGHTYELLOW_EX+'[4]']="Check the message to be send"
menu[Fore.LIGHTYELLOW_EX+'[5]']="Exit"

while True: 
    options=menu.keys()
    for entry in options: 
        print(entry, menu[entry])

    selection=input("Please Select: ") 
    if selection =='1': 
        main.singleRecipient()
        print(Fore.YELLOW+'\nEmail Sent! \n')
    elif selection == '2': 
        main.multiRecipient()
        print(Fore.YELLOW+'\nEmail Sent to multiple receivers! \n')
    elif selection == '3':
        main.checkRecipients()
    elif selection == '4':
        main.checkBodyMessage()
    elif selection == '5':
        print(Fore.YELLOW+"Thank you for using our script!")
        sleep(2) 
        break
    else: 
        print(Fore.RED+"Invalid Keyword!\n")
