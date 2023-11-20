import random

def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return midpoint
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return None

def binary_search_recursive(a_list, item):
    print(list(a_list))
    midpoint = len(a_list) // 2

    if a_list[midpoint] == item:
        return a_list[midpoint]
    elif item < a_list[midpoint]:
        return binary_search_recursive(a_list[:(midpoint)], item)
    else:
        return binary_search_recursive(a_list[(midpoint+1):], item)

    return None

if __name__ == '__main__':
    lista = []
    for i in range(0,14):
        lista.append(random.randint(1,100))
        
    lista.append(43)
    lista = sorted(lista)
    
    # print(list(lista))
    # print(binary_search(lista, 43))
    print(binary_search_recursive(lista, 2))