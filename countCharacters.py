import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {} #make an empty list dictionary

for character in message: #for each character in the message
    count.setdefault(character, 0) #add the character to the dictionary
    count[character] = count[character] + 1 #increase the value by 1 when u loop over again

print(pprint.pformat(count)) #print the dictionary of letters and their counts
