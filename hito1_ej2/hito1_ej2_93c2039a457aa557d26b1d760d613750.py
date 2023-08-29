#Contestador de celular
numero = str (input("Ingrese el numero de telefono: "))
hora = int (input("Ingrese la hora de la llamada: "))

if hora > 19 and hora <= 23:
    print ("NO CONTESTAR")
else:
    if hora > 7 and hora < 14 and str (numero [-3]) == "9" and str (numero [-2]):
         print("CONTESTAR")
    if hora > 7 and hora < 14 and str (numero [-3]) != "9" and str (numero [-2]):
         print("NO CONTESTAR")
    if hora > 17 and hora < 19 and str (numero [0:1]) != "8" and str (numero [1:2]):
         print("CONTESTAR")
    if hora > 17 and hora < 19 and str (numero [0:1]) == "8" and str (numero [1:2]):
         print("NO CONTESTAR")