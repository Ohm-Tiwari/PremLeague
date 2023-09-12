# main.py - Main work 
# This code will ask user for the year and two teams -> return result of fixtures
# Author : Ohm T

#allows code to read the database of prem league matches
import csv
#import numpy as num
#import pandas as pd
#takes year from user. Checks if valid
year = int(input("Enter season(2013-2022): "))
if 2013 <= year <= 2022:
    print("Season selected:", year)
else:
    print("Please enter a valid season.")


#takes team1
team1 = input("Enter team 1: ")
print("team 1: " + team1)

#takes team2
team2 = input("Enter team 2: ")
print("team 2: " + team2)

#Print results of matches of two teams
print(team1 + " V " + team2 + " fixtures in " + str(year))

#posts results from the created user search

def get_userid_by_accountid(account_id):
    # read the file
    file = open(r'Path\Accounts.csv')
    # convert file to Dictionary
    account_list = csv.DictReader(file)
    # print(account_list)
    # loop through the records
    for entry in account_list:
        # condition to match
        if account_id == entry['AccountId']:
            return entry['UserId']


# function to return state
def get_userstate_by_userid(userid):
    file = open(r'Path\Addresses.csv')
    address_list = csv.DictReader(file)
    for entry in address_list:
        if userid == entry['UserId']:
            return entry['State']


# input account number by user
account_num = input('Enter the account number:')
# get user id
userId = get_userid_by_accountid(account_num)
# get user state
State = get_userstate_by_userid(userId)
print(State)