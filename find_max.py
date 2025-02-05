lista=[5, 9, 2, 12, 7]

def find_max(lista):
    max=lista[0]
    for num in lista:
        if num > max:
            max=num
    return max

print(find_max(lista))

def max_fnc(lista):
    return max(lista)

print(max_fnc(lista))