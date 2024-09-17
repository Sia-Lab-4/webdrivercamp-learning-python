#!/usr/bin/python3

def replace_element(list_, index, element_to_replace):
    list_copy = list_.copy()

    if 0 <= index < len(list_copy):
        for i in range(len(list_copy)):
            if i == index:
                list_copy[i] = element_to_replace
        print("Copy: ", list_copy)
    else:
        print("Copy: ", list_copy)

    print("Original: ", list_)


list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
replace_element(list_, index, element_to_replace)

