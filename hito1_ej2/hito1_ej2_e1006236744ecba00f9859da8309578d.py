#Contestador de celular
numero = str(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))
if hora > 0 and hora < 7:
  print ("contestar")
if hora > 17 and hora <= 23:
  print ("no contestar")
else:
    if hora > 7 and hora < 14 and str(numero[-3]) == "9" and str(numero[-2]) ==
        print ("contestar")
    if hora > 7 and hora < 14 and str(numero[-3]) != "9" and str(numero[-2]) !=
        print ("contestar")
    if hora > 17 and hora < 19 and str(numero[0:1]) == "8" and str(numero[1:2]) ==
        print ("contestar")
    if hora > 17 and hora < 19 and str(numero[0:1]) != "8" and str(numero[1:2]) !=
        print ("contestar")