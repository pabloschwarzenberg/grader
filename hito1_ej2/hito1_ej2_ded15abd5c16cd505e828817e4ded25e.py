N=int(input("Ingrese numero telefonico: "))
H=float(input("Ingrese hora de la llamada separando hora de minutos con un punto: "))

if H>19:
    print("Resultado: NO CONTESTAR")
if H<=7:
    print("Resultado: CONTESTAR")
if H>=17 and H<=19:
    if N>=87700000 and N<=87799999:
        print("Resultado: NO CONTESTAR")
    else:
       print("Resultado: CONTESTAR")
if H>7 and H<14:
    if (N-(N-909))==909:
        print("Resultado: CONTESTAR")
    else:
        if H>=14 and H<17:
            print("k c yo no soi 100tifiko")
