def numero_perfecto(a):
    divisores = [i for i in range(1, a + 1) if a % i == 0]
    b = sum(divisores) - a
    if b == a:
        return True
    else:
        return False


n = 13
print(numero_perfecto(n))