# completa el código de la función
def suma_divisores(a):
    divisores=[1]
    numprimo ="primo"
    for i in range(2,a):
        if a% i == 0:
            divisores.append(i)
    if sum(divisores)==1:
            numprimo
    return numprimo
           