'''
Aryan Singhal
CIS 41A   Winter 2024
Unit H, Problem H
'''

import pickle

# Part One
class BritCoins:
    __coinValues = {"pound": 240, "shilling": 12, "penny": 1}

    def __init__(self, **kwargs):
        self.totalPennies = sum(kwargs.get(coin, 0) * value for coin, value in self.__coinValues.items())

    def __add__(self, other):
        return BritCoins(penny=self.totalPennies + other.totalPennies)

    def __sub__(self, other):
        return BritCoins(penny=max(self.totalPennies - other.totalPennies, 0))

    def __str__(self):
        pounds, remainder = divmod(self.totalPennies, 240)
        shillings, pennies = divmod(remainder, 12)
        return f"{pounds} pounds {shillings} shillings {pennies} pennies"

# Testing the BritCoins class
c1 = BritCoins(pound=4, shilling=24, penny=3)
c2 = BritCoins(pound=3, shilling=4, penny=5)
c3 = c1 + c2
c4 = c1 - c2

print(c1)
print(c2)
print(c3)
print(c4)

# Part Two
# Pickling c4
with open('britcoin_c4.pickle', 'wb') as f:
    pickle.dump(c4, f)

# Unpickling
with open('britcoin_c4.pickle', 'rb') as f:
    unpickled_c4 = pickle.load(f)

print(unpickled_c4)


'''
Execution results:

5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies
1 pounds 19 shillings 10 pennies
'''