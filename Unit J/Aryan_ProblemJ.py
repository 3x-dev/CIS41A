'''
Aryan Singhal
CIS 41A   Winter 2024
Unit J, Problem J
'''

import re

# Part 1
def search_a(data):
    pattern = r'a'
    if re.search(pattern, data):
        return "found"
    else:
        return "not found"

data = input("Enter text: ")
print(search_a(data))


# Part 2
data = input("Enter text: ")
pattern = r'b.'
matches = re.findall(pattern, data)
print(matches)


# Part 3
data = input("Enter text: ")
pattern = r' '
substrings = re.split(pattern, data)
print(substrings)


# Part 4
data = input("Enter text: ")
pattern = r'th'
result = re.sub(pattern, 'lore', data)
print(result)


'''
Execution results:

Enter text: Harry S. Truman
found
Enter text: Dwight D. Eisenhower
not found

Enter text: Dobby Rebeus Longbottom Gabrielle Albus
['bb', 'be', 'bo', 'br', 'bu']

Enter text: Bill Charlie Percy Fred George Ron Ginny
['Bill', 'Charlie', 'Percy', 'Fred', 'George', 'Ron', 'Ginny']

Enter text: thlei, th, and folk tales
lorelei, lore, and folk tales
'''