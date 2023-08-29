N=int(input("Ingrese numero telefonico:"))
H=int(input("Ingrese hora de llamada:"))
if H>=0 and H<=7:
    print("Resultado = CONTESTAR ")
elif H>7 and H<14:
    if (N-909)%1000==0:
        print("Resultado = CONTESTAR ")
    else:
        print("Resultado = NO CONTESTAR ")
elif H>=14 and H<17:
    print("Resultado = NO CONTESTAR ")
elif H>=17 and H<=19:
    if 99999>=(N-87700000):
        print("Resultado = NO CONTESTAR ")
    else:
        print("Resultado = CONTESTAR ")
elif H>19:
    print("Resultado = NO CONTESTAR ")

  