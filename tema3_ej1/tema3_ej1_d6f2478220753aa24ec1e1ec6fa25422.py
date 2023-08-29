def suma_divisores():
    n = int(input("Ingrese un N°: "))
    divisores = [1]
    for i in range(2, n + 1):
        if n % i == 0:
            divisores.append(i)

    if sum(divisores)-n == 1:
        return True