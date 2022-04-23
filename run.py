#!/usr/bin/env python3.8 

from user import User


def create_account(first_name, last_name, email, password): #Function to create a new account

    new_account = User(first_name, last_name, email, password)

    return new_account

