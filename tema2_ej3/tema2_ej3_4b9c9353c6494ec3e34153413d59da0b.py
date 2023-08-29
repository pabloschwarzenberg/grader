def numero_perfecto(a):
    Numero_Ingresado    =       a
    Acumulador          =       0
    Contador            =       0
    for divisores in range(1,Numero_Ingresado):
        if Numero_Ingresado%divisores==0:
            Acumulador = Acumulador + divisores
    if Acumulador == Numero_Ingresado:
        return True
    else:
        return False