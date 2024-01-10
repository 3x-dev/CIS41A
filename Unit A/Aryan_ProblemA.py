import math

'''
Aryan Singhal
CIS 41A   Winter 2024
Unit A, Problem A
'''

print("#1)")
a = 3 ** 2.5
print(a)

b = 2
b += 3
print(b)

c = 12
c /= 4
print(c)

d = 5 % 3
print(d)


print("\n#2)")
print(abs(5 - 7))
print(round(3.14159, 4))
print(round(186282, -2))
print(min(6, -9, -3, 0))


print("\n#3)")
num_input = input("Please enter a number: ")
number = float(num_input)
square_root = math.sqrt(number)
rounded_square_root = round(square_root, 2)
print("Square root of number rounded to 2 decimal places: ", rounded_square_root)
base_10_log = math.log10(number)
rounded_base_10_log = round(base_10_log, 2)
print("Logarithm base 10 of number rounded to 2 decimal places: ", rounded_base_10_log)

'''
Execution results:
#1)
15.588457268119896
5
3.0
2

#2)
2
3.1416
186300
-9

#3)
Please enter a number: 7.6
Square root of number rounded to 2 decimal places:  2.76
Logarithm base 10 of number rounded to 2 decimal places:  0.88
'''