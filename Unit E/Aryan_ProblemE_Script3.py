'''
Aryan Singhal
CIS 41A   Winter 2024
Unit E, Problem E
'''

# part 1
quote = "Believe you can and you're halfway there."

index = 0

while index < len(quote):
    index = quote.find('a', index)

    if index == -1:
        break

    print(f"'a' found at index {index}")
    index += 1


# part 2
num_rows = int(input("\nPlease enter the number of rows for the multiplication table: "))

for row in range(1, num_rows + 1):
    for col in range(1, row + 1):
        print(f"{row * col:4}", end='')
    print()

'''
Execution results:

'a' found at index 13
'a' found at index 16
'a' found at index 28
'a' found at index 32

Please enter the number of rows for the multiplication table: 12
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
   6  12  18  24  30  36
   7  14  21  28  35  42  49
   8  16  24  32  40  48  56  64
   9  18  27  36  45  54  63  72  81
  10  20  30  40  50  60  70  80  90 100
  11  22  33  44  55  66  77  88  99 110 121
  12  24  36  48  60  72  84  96 108 120 132 144
'''