# completa el código de la función
def suma_divisores(a):
    divisores = []
    for i in range(1,a+1):
        if a % i == 0:
          divisores.append(i)
    suma = sum(divisores)
    resultado = suma - a
    if resultado == 1:
        return(resultado,True)
    if resultado != 1:
        return(resultado,False)           