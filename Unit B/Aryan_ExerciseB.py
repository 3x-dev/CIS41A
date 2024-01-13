'''
Aryan Singhal
CIS 41A   Winter 2024
Unit B, Exercise B
'''


name = input("What is your name: ")
print(name.upper())
print(len(name))
print(name[3])
name2 = name.replace('o', 'x')
print(name2)
print(name)


quote = "Believe you can and you're halfway there."
count_a = quote.count('a')
print("Count = " + str(count_a))
indexes_of_a = []
start = 0
while True:
    index = quote.find('a', start)
    if index == -1:
        break
    indexes_of_a.append(index)
    start = index + 1
    print("a found at " + str(index))


'''
Execution results:
What is your name: George Washington
GEORGE WASHINGTON
17
r
Gexrge Washingtxn
George Washington
Count = 4
a found at 13
a found at 16
a found at 28
a found at 32
'''