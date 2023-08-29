# completa el código de la función
def suma_divisores(a):
    s = 0
    for i in range(1,a):
        if a % i == 0:
            s = s + i
    verificador = True
    if a == 2 :
        verificador = True
    elif a <=1:
        verificador = False

    else:
        for recorrido in range(2,a):
            if a % recorrido == 0:
                verificador = False    
    resultado=(s,verificador)
    return resultado
    
   