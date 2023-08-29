# completa el código de la función
def suma_divisores(a):
    numSum = 0
    for i in range(a):
        if i != 0 and a % i == 0:
            numSum += i
    if numSum == 1:
        return numSum, True
    return numSum, False


if __name__ == "__main__":
    a = eval(input())
    print(suma_divisores(a))