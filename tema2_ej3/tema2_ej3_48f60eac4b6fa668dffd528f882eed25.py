def numero_perfecto(valor):
    total = 0
    lista = []
    for numero in range(1, valor):
        if (valor%numero == 0):
             lista.append(numero)
    for numero in lista:
        total += numero
    if (total == valor):
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           