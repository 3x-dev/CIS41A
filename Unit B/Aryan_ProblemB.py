'''
Aryan Singhal
CIS 41A   Winter 2024
Unit B, Problem B
'''

print("First Script")

user_input = input("Enter a string: ")
is_upper_result = user_input.isupper()
print(is_upper_result)
is_digit_result = user_input.isdigit()
print(is_digit_result)
is_alpha_result = user_input.isalpha()
print(is_alpha_result)
haiku = "Type, type, type away.\nCompile. Run. Hip hip hooray!\nNo error today!"
print(haiku)

quote = "And now for something completely different"
print(quote[:6])
print(quote[-4:])
print(quote[14:16])
print(quote[::2])
print(quote[::-1])

pattern1 = ".~*'"
pattern2 = pattern1 + pattern1[::-1]
print(pattern2 * 5)

print("\nSecond Script")
PRICE_SMALL_BEADS = 10.20
PRICE_MEDIUM_BEADS = 8.52
PRICE_LARGE_BEADS = 7.98

def print_invoice():
    # Asking the user for input and converting it to integers
    qty_small = int(input("How many boxes of small beads do you need?: "))
    qty_medium = int(input("How many boxes of medium beads do you need?: "))
    qty_large = int(input("How many boxes of large beads do you need?: "))

    total_small = qty_small * PRICE_SMALL_BEADS
    total_medium = qty_medium * PRICE_MEDIUM_BEADS
    total_large = qty_large * PRICE_LARGE_BEADS
    total = total_small + total_medium + total_large

    print("")
    print("{:<10}{:>5}{:>17}{:>15}".format("SIZE", "QTY", "COST PER BOX", "TOTALS"))
    print("{:<10}{:>5d}{:>17.2f}{:>15.2f}".format("Small", qty_small, PRICE_SMALL_BEADS, total_small))
    print("{:<10}{:>5d}{:>17.2f}{:>15.2f}".format("Medium", qty_medium, PRICE_MEDIUM_BEADS, total_medium))
    print("{:<10}{:>5d}{:>17.2f}{:>15.2f}".format("Large", qty_large, PRICE_LARGE_BEADS, total_large))
    print("{:<10}{:>37.2f}".format("TOTAL", total))

print_invoice()

"""print("Test 1:")
print_invoice(10, 9, 8)

print("\nTest 2:")
print_invoice(5, 10, 15)"""


'''
Execution results:
First Script
Enter a string: ABC123
True
False
False
Type, type, type away.
Compile. Run. Hip hip hooray!
No error today!
And no
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.

Second Script
How many boxes of small beads do you need?: 10
How many boxes of medium beads do you need?: 9
How many boxes of large beads do you need?: 8

SIZE        QTY     COST PER BOX         TOTALS
Small        10            10.20         102.00
Medium        9             8.52          76.68
Large         8             7.98          63.84
TOTAL                                    242.52

Second Script
How many boxes of small beads do you need?: 5
How many boxes of medium beads do you need?: 10
How many boxes of large beads do you need?: 15

SIZE        QTY     COST PER BOX         TOTALS
Small         5            10.20          51.00
Medium       10             8.52          85.20
Large        15             7.98         119.70
TOTAL                                    255.90
'''