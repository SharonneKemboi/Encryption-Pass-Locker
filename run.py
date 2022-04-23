#!/usr/bin/env python3.8 

from user import User
from user import Credentials # we import user from class credentials


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

 