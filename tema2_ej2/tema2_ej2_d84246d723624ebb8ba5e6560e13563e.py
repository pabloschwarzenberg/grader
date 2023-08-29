def amigos(a,b):
    numeros_a = 0
    numeros_b = 0
    for i in range(1, a):  
        if a % i == 0:
            numeros_a += i

    for k in range(1, b):  
        if b % k == 0:
            numeros_b += k
    if numeros_a == b and numeros_b == a:
        return True
    else:
        return False

a =220
b =284
amigos(a,b)
print(amigos)
