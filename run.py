#!/usr/bin/env python3.8 

from user import User
from user import Credentials # we import user from class credentials
from termcolor import colored
from pyfiglet import Figlet


def create_account(first_name, last_name, email, password): #Function to create a new account

    new_account = User(first_name, last_name, email, password)

    return new_account


def save_account(account): #function to save account

    account.save_account()


def generate_password(account): #function to generate password
    '''
    function to generate password
    '''
    account.generate_password()


def create_credential(account_name, email, password): #function that creates new credentials

    new_credential = Credentials(account_name, email, password)

    return new_credential


def save_credentials(credential): # function that saves credentials

    credential.save_credentials()


def save_multiple_credentials(account): #function that saves multiple credentials

    account.save_multiple_credentials()


def display_credentials(): #function that displays credentials
    return Credentials.display_credentials()


def delete_credentials(credential): #function to delete credentials
    credential.delete_credentials()

#main function 
def main():
    f = Figlet(font='standard') #font using Figlet module
    print(colored(f.renderText('PASSAVER'), 'cyan')) #color using termcolor module
    print("Hola!, Welcome To Atarah's Passaver Where You Can Save Your Passwords For Various Accounts.")
    print(colored("To Get You Started, Please Create An Account or Log in:", 'blue'))
    print('\n')
    print(colored("Use these Atarah Short codes", 'green'))
    print("ca - create an account")
    print("ln - log in")
    print('\n')

    short_code = input().lower()
    if short_code == 'ca':
        print("Lets Begin by creating a special new account for you. To do that, Atarahs' PassLock Will Need Some Information From You:")
        print('\n')
        print("First Name")
        first_name = input()
        print('\n')
        print("Second Name")
        last_name = input()
        print('\n')
        print("Email Address")
        email = input()
        print('\n')
        print("Password")
        print("-"*8)
        password = input()
        print('\n')
        save_account(create_account(first_name, last_name, email, password))
        print('\n')
        print(f"Karibu {first_name}, let's get started, Are you Ready?")
        print('\n')

    elif short_code == 'ln':
        print('\n')
    

    print(colored("Use These Atarah Short Codes : cc - create a new credential, dc - display credentials details, dd - delete credentials details, fc -find credentilas, ex -exit the list", 'green'))
    short_code2 = input().lower()
    print('\n')


    if short_code2 == 'cc':
        print("New Credential")
        print('\n')

        print("Account Name")
        account_name = input()
        print('\n')

        print("Email Address or Username")
        email = input()
        print('\n')

        print("Account's Password")
        password = input()
        print('\n')

        save_credentials(create_credential(account_name, email, password))
        print(f"Account Created Successfully!! {account_name} {email} {password}")
        print('\n')

    elif short_code2 == 'dc':
        if display_credentials():
            print("Hello! Here is your credentials {first_name}")
            print('\n')

            for credential in display_credentials():
                print(
                        f"{credential.account_name} {credential.email} {credential.password}")
                print('\n')

        else:
            print('\n')
            print("Oops! Your Credentials list is empty")
            print('\n')

    print("Use these short codes : cc - create a new credentialt, dc - display credential details, fc -find credential, ex -exit credential list")
    short_code = input().lower()
    print('\n')