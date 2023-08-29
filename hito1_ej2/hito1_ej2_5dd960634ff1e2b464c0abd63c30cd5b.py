#Contestador de celular
Numero= str(input("Ingrse numero telefonico: "))
hora= int(input("Ingrese hora de la llamada: "))
if hora >0 and hora < 7:
   print("CONTESTAR")
if hora > 19 and hora <= 23:
   print("NO CONTESTAR")
else:
    if hora > 7 and hora < 14 and str(Numero[-3]) == "9" and str(Numero[-2]) == "0" and str(Numero[-1]) == "9":
      print("CONTESTAR")
    if hora > 7 and hora < 14 and str(Numero[-3]) != "9" and str(Numero[-2]) != "0" and str(Numero[-1]) != "9":
      print("CONTESTAR")    
    if hora > 17 and hora < 19 and str(Numero[0:1]) == "8" and str(Numero[1:2]) == "7" and str(Numero[2:3]) == "7":
      print("NO CONTESTAR")
    if hora > 17 and hora < 19 and str(Numero[0:1]) != "8" and str(Numero[1:2]) != "7" and str(Numero[2:3]) != "7" :
      print("NO CONTESTAR")  