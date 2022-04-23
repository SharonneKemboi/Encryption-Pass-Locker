#!/usr/bin/env python3.8 

from user import User


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
