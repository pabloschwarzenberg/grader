def amigos(a,b):
    numero1 = a
    numero2 = b

    contador = 0
    divisores1 = []
    divisores2 = []

    for divisor in range(1,numero1+1):

        if (numero1 % divisor) == 0 :

            print(divisores1)
            divisores1.append(divisor)
            contador += 1

    for divisor in range(1,numero2+1):

        if (numero2 % divisor) == 0 :


            divisores2.append(divisor)
            contador += 1
    print(divisores1)
    print(divisores2)
    if len(divisores1) > 2:
        divisores1.pop(-1)

    if len(divisores2) > 2:
        divisores2.pop(-1)
    print(divisores1)
    print(divisores2)

    if sum(divisores1) == numero2 or sum(divisores2) == numero1:
        amigos = True
    else:
        amigos = False

    return amigos