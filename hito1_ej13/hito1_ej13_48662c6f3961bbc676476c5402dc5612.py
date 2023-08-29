#Factores Primos
n = int(input())

while n != 1:
    if n % 2 == 0:
        print(2)
        n /= 2

    elif n % 3 == 0:
        print(3)
        n /= 3

    elif n % 5 == 0:
        print(5)
        n /= 5

    elif n % 7 == 0:
        print(7)
        n /= 7

    elif n % 11 == 0:
        print(11)
        n /= 11

    elif n % 13 == 0:
        print(13)
        n /= 13

    else:
        print(n)
        n /= n