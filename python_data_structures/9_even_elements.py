#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]

even_or_odd = tuple(number % 2 == 0 for number in my_list)

print(my_list)
print(even_or_odd)
