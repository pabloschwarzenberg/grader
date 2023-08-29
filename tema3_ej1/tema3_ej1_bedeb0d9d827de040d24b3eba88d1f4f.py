# completa el código de la función
def suma_divisores(a):
    sumaDivisores = 0
    for i in range(1,a):
        if a%i == 0 and i != a:
            sumaDivisores = sumaDivisores + i

    if sumaDivisores == 1:
        return sumaDivisores, True
    else:
        return sumaDivisores, False


if __name__ == "__main__":
    num = suma_divisores(1)
    print(num)

