#!/usr/bin/python3
def only_unique(list_=[]):
    list_of_uniques = set(list_)
    return sum(list_of_uniques)

if __name__=="__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
