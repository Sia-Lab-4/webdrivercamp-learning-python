#!/usr/bin/python3

def replace_element(list_, index, element_to_replace):
    
    if 0 <= index < len(list_):
        for i in range(len(list_)):
            if i == index:
                list_[i] = element_to_replace
        print(list_)
    else:
        print(list_)

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
replace_element(list_, index, element_to_replace)

