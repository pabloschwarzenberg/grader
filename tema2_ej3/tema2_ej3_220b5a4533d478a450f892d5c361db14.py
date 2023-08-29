def numero_perfecto(x):
    s = 0

    for i in range(1,x):
        if x % i == 0:
            s += i
    return s == x

    x=int(input("Ingrese valor: "))
    print(numero_perfecto(x))