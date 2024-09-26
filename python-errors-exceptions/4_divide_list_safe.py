#!/usr/bin/python3
def divide_list_safe(list_1, list_2, list_len):
    result = []

    for i in range(list_len):
        try:
            elem_1 = list_1[i]
            elem_2 = list_2[i]
            
            if not (isinstance(elem_1, (int, float)) and isinstance(elem_2, (int, float))):
                print("wrong type")
                result.append(0)
                continue
            
            if elem_2 == 0:
                print("division by 0")
                result.append(0)
                continue
            
            result.append(elem_1 / elem_2)

        except IndexError:
            print("out of range")
            result.append(0)
        
    return result

if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()
    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
