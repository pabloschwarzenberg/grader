#Contestador de celular
Numero = str(input("ingresa el Numero telefonico:"))

Hora=int(input("ingresa Hora en la que marcaste: "))
             
if Hora > 0 and Hora < 7:
             
    print("contestar")

if Hora > 19 and Hora <= 23:
             
    print("No contestar")
             
else:
    
    if Hora > 7 and Hora < 14 and str(Numero[-3]) == "9" and str(Numero[-2]) == "0"and str(Numero[-1]) == "9":
    
     print("contestar")

    if Hora > 7 and Hora < 14 and str(Numero[-3]) != "9" and str(Numero[-2]) != "0"and str(Numero[-1]) != "9":

     print("no contestar")

    if Hora > 17 and Hora < 19 and str(Numero[0:1]) == "8" and str(Numero[1:2]) == "7" and str(Numero[2:3]) == "7":
    
     print("no contestar")

    if Hora > 17 and Hora < 19 and str(Numero[0:1]) != "8" and str(Numero[1:2]) != "7" and str(Numero[2:3]) != "7":
    
     print("contestar")