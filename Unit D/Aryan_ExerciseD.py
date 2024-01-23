'''
Aryan Singhal
CIS 41A   Winter 2024
Unit D, Exercise D
'''

fruit_desserts = {
    "apple": "sauce",
    "peach": "cobbler",
    "carrot": "cake",
    "strawberry": "sorbet",
    "banana": "cream pie"
}

fruit_desserts["mango"] = "sticky rice"

fruit_desserts["strawberry"] = "shortcake"

fruit_desserts.pop("carrot", None)

print("Apple dessert:", fruit_desserts["apple"])

banana_exists = "banana" in fruit_desserts
pear_exists = "pear" in fruit_desserts
print("Banana dessert exists:", banana_exists)
print("Pear dessert exists:", pear_exists)

print("Keys in the dessert dictionary:", list(fruit_desserts.keys()))
print("Values in the dessert dictionary:", list(fruit_desserts.values()))
print("Key-value pairs in the dessert dictionary:", fruit_desserts)


capitols1 = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento"
}

capitols2 = {
    "California": "Sac.",
    "Colorado": "Denver",
    "Connecticut": "Hartford"
}

capitols1.update(capitols2)

sorted_capitols = sorted(capitols1.values())
print("Sorted capitols:", sorted_capitols)


class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha", "Miguel", "Tanya", "Hiroto", "Audry"}

class1.add("John")

students_in_both_classes = sorted(class1.intersection(class2))

all_students = sorted(class1.union(class2))

is_sasha_in_class1 = "Sasha" in class1

print("Students in both classes:", students_in_both_classes)
print("All students:", all_students)
print("Is Sasha in class1:", is_sasha_in_class1)


'''
Execution results:
Apple dessert: sauce
Banana dessert exists: True
Pear dessert exists: False
Keys in the dessert dictionary: ['apple', 'peach', 'strawberry', 'banana', 'mango']
Values in the dessert dictionary: ['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice']
Key-value pairs in the dessert dictionary: {'apple': 'sauce', 'peach': 'cobbler', 'strawberry': 'shortcake', 'banana': 'cream pie', 'mango': 'sticky rice'}
Sorted capitols: ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
Students in both classes: ['Audry', 'Tanya']
All students: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Miguel', 'Sasha', 'Tanya']
Is Sasha in class1: False
'''