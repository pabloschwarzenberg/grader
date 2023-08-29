#Contestador de celular
Telefono= int(input("Ingrese numero telefonico"))
Hora= int(input("Hora:"))
if Hora >= 0 and Hora <= 7:
   print("CONTESTAR")
if Hora > 7 and Hora <= 14:
   if(Telefono%1000)==909:
       print("CONTESTAR")
   else:
        print("NO CONTESTAR")
if Hora >= 17 and Hora <= 19:
    if(Telefono//100000)==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if Hora > 19:
    print("NO CONTESTAR")