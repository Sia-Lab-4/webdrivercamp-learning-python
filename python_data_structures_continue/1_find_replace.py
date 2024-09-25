#!/usr/bin/python3
def find_replace(original, find, replace):
    new_original = []
    for number in original:
        if number == find:
            new_original.append(replace)
        else:
            new_original.append(number)
    return new_original

if __name__=="__main__":
    original = [0, 11, 13, 9, 4, 3, 4, 7, 7, 1, 0, 9]
    modified = find_replace(original, 9, 13)
    print(f"Original: {original}")
    print(f"Modified: {modified}")
