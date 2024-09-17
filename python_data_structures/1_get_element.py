#!/usr/bin/python3
def get_element(list_, index):
    if index < 0 or index >= len(list_):
        return None
    for i, element in enumerate(list_):
        if i == index:
            print("The element retrieved is", element)
            return

list_ = [5, 4, 3, 2, 1]
index = 2
get_element(list_, index)



