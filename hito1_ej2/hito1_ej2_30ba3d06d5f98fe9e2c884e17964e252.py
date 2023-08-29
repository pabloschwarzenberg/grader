#Contestador de celular

 
Numero = str(input("ingrese los ultimos 8 digitos de su numero telefonico"))

Hora = int(input("ingrese hora de llamada"))
if Hora > 0 and Hora < 7: print("contestar")

if Hora > 19 and Hora <= 23: print("No contestar")

else:
       if Hora > 7 and Hora < 14 and str(Numero[-3]) == "9" and str(Numero[-2]) == "0" and str(Numero[-1]) == "9":
           print("contestar")
       if Hora > 7 and Hora < 14 and str(Numero[-3]) != "9" and str(Numero[-2]) != "0" and str(Numero[-1]) != "9":
           print("No contestar")
       if Hora > 17 and Hora < 19 and str(Numero[0:1]) == "8" and str(Numero[1:2]) == "7" and str(Numero[2:3]) =="7":
           print("No contestar")
       if Hora > 17 and Hora < 19 and str(Numero[0:1]) != "8" and str(Numero[1:2]) != "7" and str(Numero[2:3]) != "7":
           print("Contestar")