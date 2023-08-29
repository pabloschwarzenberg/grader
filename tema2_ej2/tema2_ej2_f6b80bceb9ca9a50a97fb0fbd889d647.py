def amigos(a,b):
    suma_divisores_de_a = 0
    suma_divisores_de_b = 0
    for i in range(1,a):
        if a%i==0:
            suma_divisores_de_a += i
    for x in range(1,b):
        if b%x==0:
            suma_divisores_de_b += x
    return suma_divisores_de_a==b and suma_divisores_de_b==a
    if suma_divisores_de_a ==b and suma_divisores_de_b ==a:
        return True
    else:
        return False