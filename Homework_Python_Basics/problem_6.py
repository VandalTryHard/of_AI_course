# Дана следующая строка:
# string = '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,]'
# Пройдя по символам строки, переведите строку в список.
string = '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,]'
string = string.replace(',', '')
string = string[1:-1]
list0 = string.split()
print(string)
print(type(string))
print(list0)
print(type(list0))
