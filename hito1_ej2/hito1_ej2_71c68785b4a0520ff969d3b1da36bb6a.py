#Contestador de celular
nro=int(input("ingrese el numero telefonico (8 numeros): "))
hora=int(input("ingrese hora de la llamada: "))

if hora >=0 and hora < 7:
    print( "CONTESTAR")
elif hora < 14:
    if nro % 1000 == 909:
        print(" CONTESTAR")
    else:
        print(" NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    if str(nro).startswith ('877'):
        print("NO CONTESTAR")
    else:
        print(" CONTESTAR ")
else:
    print("NO CONTESTAR")      