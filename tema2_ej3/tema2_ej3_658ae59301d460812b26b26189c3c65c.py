def numero_perfecto(n):
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    if (sum(divisores) - n) == n:
        return("True")
    else:
        return("False")