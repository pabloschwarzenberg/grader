#Contestador de celular
NC= str(input("Escriba el número de teléfono:"))
H= int(input("Escriba la hora de la llamada:"))

if H>0 and H<7:
  print("CONTESTAR")

elif H > 7 and H < 14 and str(NC[-3]) != "9" and str(NC[-2]) != "0" and str(NC[-1])!= "9":
  print("NO CONTESTAR")

elif H > 7 and H < 14 and str(NC[-3]) == "9" and str(NC[-2]) == "0" and str(NC[-1]) == "9":
  print("CONTESTAR")

elif H > 17 and H < 19 and str(NC[0:1]) != "8" and str(NC[1:2]) != "7" and str(NC[2:3]) != "7" :
  print("CONTESTAR")

elif H > 17 and H < 19 and str(NC[0:1]) == "8" and str(NC[1:2]) == "7" and str(NC[2:3]) == "7":
  print("NO CONTESTAR")

elif H > 19:
  print("NO CONTESTAR")
#98927674 20
