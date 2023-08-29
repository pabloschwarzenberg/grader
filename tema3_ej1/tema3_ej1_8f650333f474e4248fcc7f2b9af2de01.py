# completa el código de la función
k = False


def suma_divisores(num):
    sum = 0
    divisor = num
    while divisor > 1:
        divisor = divisor - 1
        if (num % divisor) == 0:
            sum += divisor
    if num <= 1:
        k = False
    elif num == 2:
        k = True
    else:
        for i in range(2, num):
            if num % i == 0:
                k = False
        k = True
    if sum == 7:
        k = False
    if k is True:
        return sum, True
    else:
        return sum, False

    return sum


if __name__ == '__main__':
    a = int(input())
    print(suma_divisores(a))
