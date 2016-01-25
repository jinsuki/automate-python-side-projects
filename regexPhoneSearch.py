# \d = digit from 0 to 9; \d\d\d-\d\d\d-\d\d\d\d like phone number
# {3} = match this pattern 3-times; \d{3} = \d\d\d; \d{3}-\d{3}-\d{4}

import re

phoneNumRegex = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone Number Found: ' + mo.group())
print('Area Code: ' + mo.group(1))
