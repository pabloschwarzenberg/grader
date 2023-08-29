#Contestador de celular
Numerotelefonico = str(input("ingresa el Numero telefonico:"))

Hora=int(input("ingresa Hora en la que marcaste: "))
             
if Hora > 0 and Hora < 7:
             
    print("contestar")

if Hora > 19 and Hora <= 23:
             
    print("No contestar")
             
else:
    
    if Hora > 7 and Hora < 14 and str(Numerotelefonico[-3]) == "9" and str(Numerotelefonico[-2]) == "0"and str(Numerotelefonico[-1]) == "9":
    
     print("contestar")

    if Hora > 7 and Hora < 14 and str(Numerotelefonico[-3]) != "9" and str(Numerotelefonico[-2]) != "0"and str(Numerotelefonico[-1]) != "9":

     print("no contestar")

    if Hora > 17 and Hora < 19 and str(Numerotelefonico[0:1]) == "8" and str(Numerotelefonico[1:2]) == "7" and str(Numerotelefonico[2:3]) == "7":
    
     print("no contestar")

    if Hora > 17 and Hora < 19 and str(Numerotelefonico[0:1]) != "8" and str(Numerotelefonico[1:2]) != "7" and str(Numerotelefonico[2:3]) != "7":
    
     print("contestar")      