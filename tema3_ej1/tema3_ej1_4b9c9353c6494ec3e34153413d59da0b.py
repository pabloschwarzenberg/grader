# completa el código de la función
def suma_divisores(a):
    Numero_Ingresado    =       a
    Acumulador          =       0
    Contador            =       0
    for divisores in range(1,Numero_Ingresado):
        if Numero_Ingresado%divisores==0:
            Acumulador = Acumulador + divisores
    if Acumulador == 1:
        return Acumulador,True
    else:
        return Acumulador,False