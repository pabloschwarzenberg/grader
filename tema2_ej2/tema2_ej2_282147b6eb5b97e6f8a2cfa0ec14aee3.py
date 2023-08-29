# completa el código de la función
def amigos(a, b):
    suma1 = 0
    suma2 = 0
    for i in range(1, (a // 2) + 1):
        if (a % i) == 0:
            suma1 = suma1 + i
            i = i + 1
    for i in range(1, (b // 2) + 1):
        if (b % i) == 0:
            suma2 = suma2 + i
        i = i + 1
    if suma1 == b and suma2 == a:
        return True
    else:
        return False
a=5
b=8
#a = int(input("Ingrese el primer numero: "))
#b = int(input("Ingrese el segundo numero: "))
print(amigos(a,b))