def suma_divisores(a):
    divisores = []
    contador = 0
    for i in range(1, a):
        if a % i == 0:
            divisores.append(i)
    for k in range(1, a + 1):
        if a % k == 0:
            contador += 1
    if contador == 2:
        return sum(divisores), True
    else:
        return sum(divisores), False





if __name__ == "__main__":
    a = int(input("Ingrese numero: "))
    print(suma_divisores(a))
