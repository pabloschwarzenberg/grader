def numero_perfecto(n):
    divisores = [1]
    for i in range(2,n+1):
        if n%i ==0:
            divisores.append(i)

    if sum(divisores)-n ==n:
        return True
    else:
        return False

numero = numero_perfecto(8)
