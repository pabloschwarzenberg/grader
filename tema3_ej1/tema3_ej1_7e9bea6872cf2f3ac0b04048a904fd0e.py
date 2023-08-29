# completa el código de la función
def suma_divisores(n):
    divisores = [1]

    for i in range(2,n+1):
        if n%i ==0:
            divisores.append(i)

    if sum(divisores) %2 :
        return sum(divisores)-n, False
    else:
        return sum(divisores)-n, True

resultados = suma_divisores(1)
print(resultados)
           