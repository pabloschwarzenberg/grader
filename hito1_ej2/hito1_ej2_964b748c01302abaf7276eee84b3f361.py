#Contestador de celular
numero = input("teléfono:")
hora = int(input("hora:"))
Cantidad = numero[0:8]
excluyente = numero[5:8]

if numero == Cantidad: 
       if(excluyente == str("909")) and (hora <= 14) and (hora >= 8):
           print("CONTESTAR")
       elif (hora >= 0) and (hora <= 7):
           print ("Es una emergencia, contesta")
       elif (hora == 17) and (hora == 19) and not (excluyente == str ("877")):
             print("contestar mas tarde")            
       else: 
           print("no contestar")
else: 
    print("numero incorrecto")
        