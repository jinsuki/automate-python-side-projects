#! /usr/bin/env python3
# bulletPointAdder.py - Adds bulletpoints to the start
# of each line copied onto the clipboard

import pyperclip
text = pyperclip.paste() # saves the pasted text into a variable object

# TODO: separate lines and add stars.
# Separate lines and add stars.

lines = text.split('\n') # split the line when \n is found

for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # adds star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
