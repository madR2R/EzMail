import os
os.system('cls')

#Colorama
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#smtp module to send emails
import smtplib
from email.message import EmailMessage


#Account information saved on .env
from dotenv import dotenv_values
CONFIG = dotenv_values(".env")

#Getting the Account information
emailAddress = CONFIG['EMAIL_USER']
emailPassword = CONFIG['EMAIL_PASSWORD']

#Recipients
message = EmailMessage()
message['From'] = emailAddress



#For Single Recipient
def singleRecipient():
    message['To'] = input('Enter Recipient: ')
    message['Subject'] = input('Enter the subject of the email: ')
    
    #The message to be send
    with open('body.txt', 'r') as body:
        message.set_content(body.read())

    #Asking User if attachment is needed
    while True:
        selection = input("Is there an attachment to be send? y/n: ")

        if selection == 'y':
            locationOfFile = input("Enter the directory of the file: ")

            with open(locationOfFile,'rb') as f:
                fileData = f.read()
                fileName = f.name

                message.add_attachment(fileData, maintype='application', subtype='octet-stream', filename=fileName)
            
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(emailAddress, emailPassword)

                smtp.send_message(message)
                break

        elif selection == 'n':
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(emailAddress, emailPassword)

                smtp.send_message(message)
                break
        else:
            print(Fore.RED+"Invalid Keyword!")

#Multiple Recipient
def multiRecipient():
    
    #Check if the text file is empty
    filesize = os.path.getsize("multipleRecipient.txt")
    if filesize == 0:
        print(Fore.RED+"Text Document is empty!")
    else:
        with open('multipleRecipient.txt', 'r') as recipients:
            recipient = []
            count = 1
            for line in recipients:
                strippedLine = line.strip()
                recipient.append(strippedLine)

        #Multiple Recipients
        message['Subject'] = input('Enter Subject of the Email: ')
        message['To'] = ", ".join(recipient)

        #The message to be send
        with open('body.txt', 'r') as body:
            message.set_content(body.read())

    #Asking User if attachment is needed
    while True:
        selection = input("Is there an attachment to be send? y/n: ")

        if selection == 'y':
            locationOfFile = input("Enter the directory of the file: ")

            with open(locationOfFile,'rb') as f:
                fileData = f.read()
                fileName = f.name

                message.add_attachment(fileData, maintype='application', subtype='octet-stream', filename=fileName)
            
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(emailAddress, emailPassword)

                smtp.send_message(message)
                break
            
        elif selection == 'n':
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(emailAddress, emailPassword)

                smtp.send_message(message)
                break
        else:
            print(Fore.RED+"Invalid Keyword!")

def checkBodyMessage():
    filesize = os.path.getsize("multipleRecipient.txt")
    if filesize == 0:
        print(Fore.RED+"Text Document is empty!\n")
    else:
        with open('body.txt', 'r') as body:
            print(Fore.YELLOW+"Here is the body of the email to be send:\n\n"+Fore.LIGHTWHITE_EX+body.read()+"\n")

def checkRecipients():
    filesize = os.path.getsize("multipleRecipient.txt")
    if filesize == 0:
        print(Fore.RED+"No recipients saved! Please input recipients at multipleRecipient.txt")
    else:
        with open('multipleRecipient.txt', 'r') as body:
            print(Fore.YELLOW+"Here is the list of Recipients saved on multipleRecipient.txt:\n\n"+Fore.LIGHTWHITE_EX+body.read()+"\n")

def main():
    singleRecipient()
    # multiRecipient()
    # checkBodyMessage()
    # checkRecipients()

if __name__ == "__main__":
    main()