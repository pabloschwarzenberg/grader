def numeros_amigos(x, y):
    suma_x = 0
    suma_y = 0
    for i in range(1, x):
        if x % i == 0:
            suma_x += i

    for k in range(1, y):
        if y % k == 0:
            suma_y += k

    return suma_x == y and suma_y == x
    return True

if numeros_amigos is True:
    print("Son numeros amigos")
else:
    print("No son numeros amigos")