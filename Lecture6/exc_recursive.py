def sum_list(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sum_list(lista[1:])

lista = ["mapp1","Mapp2","mapp hej","mapp world","mapp"]
print(sum_list(lista))


# X to the power of Y
def power(x,y):
    if y == 1:
        return x
    else:
        return x * power(x, y-1)
    
print(power(4,6))


# Reverse list
def reverse_list(lista):
    if len(lista) == 1:
        return lista
    else:
        return [lista[-1]] + reverse_list(lista[:-1])
    
print(list(lista))
print(list(reverse_list(lista)))


