#Contestador de celular
n = str(input("Ingrese un número de telefono:"))
h = int(input("Ingrese una hora de llamada:"))


if h > 0 and h < 7:


  print("Contestar")


if h > 19 and h <= 23:


  print("No contestar")



else:

  if h > 7 and h < 14 and str(n[-3]) == "9" and str(n[-2]) == "0" and str(n[-1]) == "9":


    print("Contestar")

  if h > 7 and h < 14 and str(n[-3]) != "9" and str(n[-2]) != "0" and str(n[-1]) != "9":


    print("No contestar")

  if h > 17 and h < 19 and str(n[0:1]) == "8" and str(n[1:2]) == "7" and str(n[2:3]) == "7":


    print("No contestar")

  if h > 17 and h < 19 and str(n[0:1]) != "8" and str(n[1:2]) != "7" and str(n[2:3]) != "7":


    print("Contestar")
     