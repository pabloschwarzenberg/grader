def suma_divisores():
    a = 12
    divisores = [1]

    for i in range(2, a + 1):
        if a % i == 0:
            divisores.append(i)
    n_a = sum(divisores)
 
    
    b = 28
    divisores_b = [1]

    for i in range(2, b + 1):
        if b % i == 0:
            divisores_b.append(i)
    n_b = sum(divisores_b)


    if n_a == b:
        print(True)
    elif n_b == a:
        print(True)
    else:
        print(False)

suma_divisores()
