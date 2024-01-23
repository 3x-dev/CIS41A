'''
Aryan Singhal
CIS 41A   Winter 2024
Unit D, Problem D
'''

triangle_numbers = [n * (n + 1) // 2 for n in range(1, 11)]

print("First 10 Triangle numbers: \n" + str(triangle_numbers))


class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"}

students_in_all_classes = class1.intersection(class2, class3)
sorted_students_in_all_classes = sorted(students_in_all_classes)

all_students = class1.union(class2, class3)
sorted_all_students = sorted(all_students)

students_in_class1_only = class1 - (class2.union(class3))
sorted_students_in_class1_only = sorted(students_in_class1_only)

students_in_class2_not_class1 = {student for student in class2 if student not in class1}
sorted_students_in_class2_not_class1 = sorted(students_in_class2_not_class1)

print("Students in all three classes: " + str(sorted_students_in_all_classes))
print("All students: " + str(sorted_all_students))
print("Students in class1 but not class2 or class3: " + str(sorted_students_in_class1_only))
print("Students in class2 but not class1: " + str(sorted_students_in_class2_not_class1))


movie_info = ("Casablanca", 1942, "romantic drama")
title, year, genre = movie_info

print("The genre of my favorite movie is: " + str(genre))


from collections import namedtuple

Movie = namedtuple("Movie", ["title", "year", "genre"])
casablanca = Movie("Casablanca", 1942, "romantic drama")

print("My favorite movie is: " + str(casablanca.title))


'''
Execution results:

'''