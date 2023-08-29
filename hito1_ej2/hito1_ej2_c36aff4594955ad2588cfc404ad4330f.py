#Contestador de celular
numero = input("Ingrese el teléfono:")
hora = int(input("Ingrese la hora:"))
cantidad = numero[0:8]
excluyente = numero[5:8]

if numero == cantidad:
       if (hora >= 0) and (hora <= 7):
           print ("Es una emergencia, contesta")
       elif(excluyente == str("909")) and (hora <= 14) and (hora >= 8):
           print("CONTESTAR")
       elif (hora == 17) and (hora == 19) and not (excluyente == str("877")):
             print("Contestar más tarde")
       else:
           print("NO CONTESTAR")
else:
    print("Numero equivocado")