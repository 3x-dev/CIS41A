'''
Aryan Singhal
CIS 41A   Winter 2024
Unit C, Problem C
'''

print("First Script")

list1 = []
list1.extend([1, 3, 5])
list1[1], list1[2] = list1[2], list1[1]

print("d) Items in list1:")
for item in list1:
    print(item)

list2 = [1, 2, 3, 4]

list3 = list1 + list2

print("g) list3 is:", list3)

print("h) list3 contains a 3:", 3 in list3)

count_of_3s = list3.count(3)
print("i) list3 contains", count_of_3s, "3s")

index_of_first_3 = list3.index(3)
print("j) The index of the first 3 contained in list3 is", index_of_first_3)

first3 = list3.pop(index_of_first_3)
print("k) first3 =", first3)

list4 = sorted(list3)

print("m) list3 is now:", list3)

print("n) list4 is:", list4)

sliced_list = list3[1:4]
print("o) Slice of list3 is:", sliced_list)

length_of_list3 = len(list3)
print("p) Length of list3 is", length_of_list3)

max_value_of_list3 = max(list3)
print("q) The max value in list3 is", max_value_of_list3)

list3.sort()
print("r) Sorted list3 is:", list3)

list5 = [list1, list2]

print("t) list5 is:", list5)

print("u) Value 4 from list5:", list5[1][3])


print("\nSecond Script")

a = 9
b = 14

print("a) binary of a =", bin(a))
print("b) binary of b =", bin(b))

result_and = a & b
print("c) binary of a & b =", bin(result_and))

result_or = a | b
print("d) binary of a | b =", bin(result_or))


'''
Execution results:

'''