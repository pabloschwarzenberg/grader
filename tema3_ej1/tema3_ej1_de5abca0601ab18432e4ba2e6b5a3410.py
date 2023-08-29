def suma_divisores(a):
    numero = 0
    divisores_a = [0]
    for i in range(a):
        x = i + 1
        if a % x == 0:
            divisores_a.append(x)
    


    divisores_a.remove(a)
    print(divisores_a)
    for i in divisores_a:
        numero += i
    print(numero)

    if numero == 1:
        return numero,True
    if numero == 0:
        return  numero,False
    if numero >= 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return numero,True
            else:
                return numero,False