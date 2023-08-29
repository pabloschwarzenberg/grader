cifra=input("Ingrese un valor de hasta 4 digitos:")
if len(cifra) == 1:
    print("La descomposicion es:" + str(cifra[0])+"U")
if len(cifra) == 2:
    print("La descomposicion es:" + str(cifra[0])+"D +" + str(cifra[1])+"U")
if len(cifra) == 3:
    print("La descomposicion es:" + str(cifra[0])+"C +" + str(cifra[1])+"D +" + str(cifra[2])+"U")
if len(cifra) == 4:
    print("La descomposicion es:" + str(cifra[0])+"M +" + str(cifra[1]) + "C +" + str(cifra[2]) + "D +" + str(cifra[3]) + "U")