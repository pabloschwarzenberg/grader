# completa el código de la función
def suma_divisores(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum = sum + i
    contador = 0
    for i in range(1, a + 1):
        if a % i == 0:
            contador += 1
    if contador == 2:
        return sum,True
    else:
        return sum,False