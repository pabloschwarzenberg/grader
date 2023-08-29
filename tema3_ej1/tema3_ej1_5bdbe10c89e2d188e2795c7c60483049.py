# completa el código de la funcióndef suma_divisores(a):
def suma_divisores(a):
    i = a - 1
    suma = 0
    while i > 0 :
        if a%i == 0 :
            suma = suma + i
            i = i - 1
        else:
            i = i - 1
            
    if suma == 1 :
        return suma, True
    else:
        return suma, False
           