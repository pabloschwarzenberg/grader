def numero_perfecto(a):
    perfecto = False
    divisores = []
    
    for c in range(1, a-1):
        b = a % c
        if b == 0:
            divisores.append(c)
    Sumar = sum(divisores)
    if Sumar == a:
        perfecto = True

    return perfecto
    
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))