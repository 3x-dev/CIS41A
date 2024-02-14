'''
Aryan Singhal
CIS 41A   Winter 2024
Unit G, Exercise G
'''

# Part 1
with open("ZenOfPython.txt", "w") as file:
    file.write("Beautiful is better than ugly.\n")
    file.write("Explicit is better than implicit.\n")

with open("ZenOfPython.txt", "a") as file:
    file.write("Readability counts.\n")
    file.write("If the implementation is hard to explain, it's a bad idea.\n")

with open("ZenOfPython.txt", "r") as file:
    contents = file.read()

print(contents)


# Part 2
import csv

with open('Cities.csv', mode='r') as file:
    reader = csv.DictReader(file)
    city_data = {}
    
    for row in reader:
        key = (row['City'], row['State'])
        city_data[key] = row['Population']

for key, population in city_data.items():
    print(f"{key[0]} {key[1]} {population}")

city = input("\nPlease enter a city: ")
state = input("Please enter a state: ")
key = (city, state)

if key in city_data:
    print(f"{city} {state} has a population of {city_data[key]}")
else:
    print(f"Sorry, could not find {city}, {state}.")


'''
Execution results:

Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.

Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064

Please enter a city: Dublin
Please enter a state: California
Dublin California has a population of 46036
'''