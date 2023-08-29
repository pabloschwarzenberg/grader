def amigos(a, b):
    i = 0
    n=1
    n= a % n == 0
    while a >= n:
        n = n + i
        divisores_a = []
        divisores_a.append(n)
        i = i + 1

        break
    suma = 0
    for i in divisores_a:
        suma += i
        suma1 = suma
        break
    i = 0
    m=1
    m= b % m == 0
    while b >= m:
        m = m + i
        divisores_b = []
        divisores_b.append(m)
        i = i + 1
        break
    suma3 = 0
    for i in divisores_b:
        suma3 += i
        suma4 = suma3
        break
    if suma4 == a or suma1 == b:
        return True
    else:
        return False


if __name__ == "__main__":
    a = int(input("Ingrese un número:"))
    b = int(input("Ingrese un número:"))
    print(amigos(a, b), "")