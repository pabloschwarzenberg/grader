# completa el código de la función
def suma_divisores(a):
    esPrimo = False
    divisores = 0
    suma = []
    i = 1
    while i < a:
        if a%i == 0:
            divisores += 1
            suma.append(i)
            i += 1
        else:
            i += 1
    suma = sum(suma)
    if divisores == 1:
        esPrimo = True
    return suma, esPrimo
 
  
