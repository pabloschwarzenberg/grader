# completa el código de la función
def suma_divisores(a):
    divisores = []
    for i in range(1,a):
        if a%i==0:
            divisores.append(i)
    resultado=sum(divisores)
    if resultado==1:
        return resultado,True
    else:
        return resultado, False

print(suma_divisores(28))