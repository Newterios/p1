# sallaries = [10000, 20000, 40000]
# sallaries_updated = list(map(lambda x: x * 1.1, sallaries))
# print(sallaries_updated)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)


# names = ["anna", "ivan", "sergey", "maria"]
# names_corect = list(map(lambda x: x.capitalize(), names))
# print(names_corect)


# task 4

# def password_check(x):
#     a = [0, 0]
#     for i in x:
#         if i.isupper():
#             a[0] = 1
#         if i.isdigit():
#             a[1] = 1
#     return all(a)


# password = ["Qwerty123", "gfdg223", "12", " "]
# corect_passwords = list(filter(lambda x: password_check(x), password))
# print(corect_passwords)


# task5

# lines = ["Hello", "", "World", "", "Python"]
# lines_without_null_str = list(filter(lambda x: x != "", lines))
# print(lines_without_null_str)


# Task 6

# ages = [17, 18, 0, 22]
# ages_reduced = list(filter(lambda x: x >= 18, ages))
# print(ages_reduced)


# Task 7

# numbers = [17, 18, 0, 22, 5]
# numbers_reduced = list(filter(lambda x: x % 5 == 0 and x != 0, numbers))
# print(numbers_reduced)


# Task8

# prices = [150, 300, 550, 110]
# reduced_prices = list(filter(lambda x: (x * 0.9) > 300, prices))
# print(reduced_prices)


# Task 9

# words = ["apple", "banana", "orange"]
# words_reduced1 = list(filter(lambda x: x.startswith("a") or x.startswith("b"), words))
# words_reduced = list(map(lambda x: x.upper(), words_reduced1))
# print(words_reduced)


# Task 10

# students = [{"name": "A", "grade": 55}, {"name": "Aitbek", "grade": 100}]
# sum_of_grades = 0
# for i in students:
#     sum_of_grades += i["grade"]
# average = sum_of_grades / len(students)
# students_reduced = list(filter(lambda x: x["grade"] >= average, students))
# print(students_reduced)
