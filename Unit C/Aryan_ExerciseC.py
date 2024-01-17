'''
Aryan Singhal
CIS 41A   Winter 2024
Unit C, Exercise C
'''

list1 = [2, 4.1, 'hello']

list2 = list1.copy()

import copy
list3 = copy.deepcopy(list1)

list1_eq_list2 = list1 == list2
list1_eq_list3 = list1 == list3
list2_eq_list3 = list2 == list3

list1_is_list2 = list1 is list2
list1_is_list3 = list1 is list3
list2_is_list3 = list2 is list3

print("list1 == list2:", list1_eq_list2)
print("list1 == list3:", list1_eq_list3)
print("list2 == list3:", list2_eq_list3)
print("list1 is list2:", list1_is_list2)
print("list1 is list3:", list1_is_list3)
print("list2 is list3:", list2_is_list3)
print("list1 ID:", id(list1))
print("list2 ID:", id(list2))
print("list3 ID:", id(list3))

list1.append(8)

list2.insert(1, 'goodbye')

list3.pop(0)

print("list1 printed:", list1)
print("list2 printed:", list2)
print("list3 printed:", list3)

'''
Execution results:
list1 == list2: True
list1 == list3: True
list2 == list3: True
list1 is list2: False
list1 is list3: False
list2 is list3: False
list1 ID: 140606573950080
list2 ID: 140606573941312
list3 ID: 140606610450240
list1 printed: [2, 4.1, 'hello', 8]
list2 printed: [2, 'goodbye', 4.1, 'hello']
list3 printed: [4.1, 'hello']
'''