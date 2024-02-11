'''
Aryan Singhal
CIS 41A   Winter 2024
Unit F, Problem F
'''

# Part One: Invoice Function
def invoice(unitPrice, quantity, shipping=10, handling=5):
    cost = unitPrice * quantity
    total = cost + shipping + handling
    print(f"Cost (unitPrice x quantity) = {cost}")
    print(f"Shipping = {shipping}")
    print(f"Handling = {handling}")
    print(f"Total = {total}")

# Part Two: Print Group Members Function
def printGroupMembers(groupName, *args):
    print(f"Members of {groupName}")
    for name in args:
        print(name)

# Part Three: Overseer System Function
def overseerSystem(**kwargs):
    if "temperature" in kwargs and kwargs["temperature"] > 500:
        print(f"Warning: temperature is {kwargs['temperature']}")
    if "CO2level" in kwargs and kwargs["CO2level"] > 0.15:
        print(f"Warning: CO2level is {kwargs['CO2level']}")
    if "miscError" in kwargs:
        print(f"Misc error #{kwargs['miscError']}")

# Part Four: Baseball Simulation
import random

def out():
    print("Out")
    return 0

def single():
    print("Single")
    return 1

def double():
    print("Double")
    return 2

def triple():
    print("Triple")
    return 3

def homerun():
    print("Homerun")
    return 4

outcomes = [out, single, double, triple, homerun]
probabilities = [70, 18, 5, 1, 6]

def simulate_baseball():
    outs = 0
    runs = 0
    bases = [0, 0, 0]

    while outs < 3:
        outcome_function = random.choices(outcomes, weights=probabilities, k=1)[0]
        result = outcome_function()

        if result == 0:
            outs += 1
        else:
            new_bases = [0, 0, 0]
            for i in range(3, 0, -1):
                if i - result < 0:
                    runs += bases[i-1]
                else:
                    new_bases[i-result] = bases[i-1]
            if result > 0:
                new_bases[result-1] = 1
            bases = new_bases

    print(f"Runs scored: {runs}")


invoice(20, 4, shipping=8)
invoice(15, 3, handling=15)
printGroupMembers("Group A", "Li", "Audry", "Jia")
groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
printGroupMembers(*groupB)
overseerSystem(temperature=550)
overseerSystem(temperature=475)
overseerSystem(temperature=450, miscError=404)
overseerSystem(CO2level=.17)
overseerSystem(CO2level=.2, miscError=418)
simulate_baseball()


'''
Execution results:

Cost (unitPrice x quantity) = 80
Shipping = 8
Handling = 5
Total = 93
Cost (unitPrice x quantity) = 45
Shipping = 10
Handling = 15
Total = 70
Members of Group A
Li
Audry
Jia
Members of Group B
Sasha
Migel
Tanya
Hiroto
Warning: temperature is 550
Misc error #404
Warning: CO2level is 0.17
Warning: CO2level is 0.2
Misc error #418
Double
Out
Out
Double
Out
Runs scored: 0
'''