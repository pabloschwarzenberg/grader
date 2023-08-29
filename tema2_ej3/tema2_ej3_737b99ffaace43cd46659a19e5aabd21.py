def numero_perfecto(a):
    s = 0
    for indice in range(1,a):
        if a % indice == 0:
            s += indice


    if a == s:
        return True
    else:
        return False


if __name__ ==" __main__ ":
    a=int(input("Ingrese el número a validar: "))
    print(numero_perfecto(a))
