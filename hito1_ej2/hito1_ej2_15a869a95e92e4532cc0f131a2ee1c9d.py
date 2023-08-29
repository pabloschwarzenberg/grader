#Contestador de celular
Numero = str (input("Ingrese numero telefonico: "))

Hora = int (input("Ingrese hora de la llamada: "))

if Hora > 19 and Hora <= 23:
    print ("NO CONTESTAR")
else:
    if Hora > 7 and Hora < 14 and str (Numero [-3]) == "9" and str (Numero [-2]):
         print("CONTESTAR")
    if Hora > 7 and Hora < 14 and str (Numero [-3]) != "9" and str (Numero [-2]):
         print("NO CONTESTAR")
    if Hora > 17 and Hora < 19 and str (Numero [0:1]) != "8" and str (Numero [1:2]):
         print("CONTESTAR")
    if Hora > 17 and Hora < 19 and str (Numero [0:1]) == "8" and str (Numero [1:2]):
         print("NO CONTESTAR")