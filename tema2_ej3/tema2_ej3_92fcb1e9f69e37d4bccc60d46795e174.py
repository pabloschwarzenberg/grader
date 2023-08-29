def numero_perfecto(a):
    total = 0
    lista = []
    for numero in range(1, a):
        if (a%numero == 0):
             lista.append(numero)
    for numero in lista:
        total += numero
    if (total == a):
        return True
    else:
        return False
           