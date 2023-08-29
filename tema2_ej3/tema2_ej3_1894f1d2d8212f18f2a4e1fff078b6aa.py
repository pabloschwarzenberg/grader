def numero_perfecto(val):
    total = 0
    lista = []
    for numero in range(1, val):
        if (val%numero == 0):
             lista.append(numero)
    for numero in lista:
        total += numero
    if (total == val):
        return True
    else:
        return False
