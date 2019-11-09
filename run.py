#!/usr/bin/env python3.6
from locker import *

def create_account(user_name, passsword):
    '''
    Function to create a new user account
    '''

    new_user = User(user_name, passsword)
    return new_user

def save_account(user):
    '''
    Function to save user account
    '''
    User.create_account()

def login(user_name, passsword):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(user_name, passsword)

def create_credential(account_name, passsword):

    '''
    Function to create a new credential
    '''
    new_credential = Credential(account_name, passsword)
    return new_credential

def save_credential(credential):
    '''
    Function to save a credentials
    '''
    return Credential.save_credential()

def find_credential(account_name):
    return Credential.find_by_account_name(account_name)

def view_credential():
    return Credential.view_all_credentials()

def delete_credential():
    return Credential.delete_credential()
