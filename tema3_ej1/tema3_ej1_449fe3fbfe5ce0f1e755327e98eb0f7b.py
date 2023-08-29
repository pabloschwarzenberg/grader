# completa el código de la función
def suma_divisores(a):
    divisores = []
    for n in range(1,a):
        if (a%n)==0:
            divisores.append(n)
    sum = 0
    for d in divisores:
        sum = sum + d
    if sum==1:
        primo = True
    else:
        primo = False

    return sum, primo
           