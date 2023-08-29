def sonAmigos(num1, num2):
    suma1 = 0
    suma2 = 0
    for i in range(1, num1):
        if num1 % i == 0:
            suma1 += i
    for i in range(1, num2):
        if num2 % i == 0:
            suma2 += i
    if suma1 == num2 and suma2 == num1:
        return True
    else:
        return False

print(sonAmigos(220, 284))
print(sonAmigos(6, 8))
print(sonAmigos(6, 9))