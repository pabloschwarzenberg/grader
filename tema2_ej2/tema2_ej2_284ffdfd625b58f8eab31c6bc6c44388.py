def numeros_amigos(x, y):
    suma x = 0
    suma y = 0
    for i in range(1, x):
        if x % i == 0:
            suma x += i
    for k in range(1, y):
        if y % k == 0:
            suma y += k
    return suma x == y and suma y == x

print(numeros_amigos(220, 284)) # True
print(numeros_amigos(1184, 1210)) # True
print(numeros_amigos(2620, 2924)) # True
print(numeros_amigos(5020, 5564)) # True
print(numeros_amigos(6232, 6368)) # True