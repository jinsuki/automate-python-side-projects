#! /usr/bin/env python3
# pw.py - A simple password locker program
#
# This program takes in an ID from the command line (argv1), and
# searches through a dictionary to retrieve the correct password.
#
# To use on OSX:
# 1. Save to a directory
# 2. Point terminal towards same directory
# 3. Type using archetype - ./runProgram yourID

PASSWORDS = {'email-id': 'password123',
             'blog-id': 'password234',
             'school-id': 'password345'}

import sys, pyperclip
if len(sys.argv) < 2: # checks that you have an argument
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account]) #copies password to clipboard (CMD + C)
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
