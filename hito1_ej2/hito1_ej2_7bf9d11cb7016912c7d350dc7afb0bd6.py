#Contestador de celular
#inicio#
numero = str(input("Ingrese numero telefonico:"))

hour = int(input("Ingrese hora de la llamada:"))
#procedimiento#
if hour > 0 and hour < 7:

  print("CONTESTAR")

if hour > 19 and hour <= 23:

  print("NO CONTESTAR")

else:

  if hour > 7 and hour < 14 and str(numero[-3]) == "9" and str(numero[-2]) == "0" and str(numero[-1]) == "9":

    print("CONTESTAR")

  if hour > 7 and hour < 14 and str(numero[-3]) != "9" and str(numero[-2]) != "0" and str(numero[-1]) != "9":

    print("NO CONTESTAR")

  if hour > 17 and hour < 19 and str(numero[0:1]) == "8" and str(numero[1:2]) == "7" and str(numero[2:3]) == "7":

    print("NO CONTESTAR")

  if hour > 17 and hour < 19 and str(numero[0:1]) != "8" and str(numero[1:2]) != "7" and str(numero[2:3]) != "7":

    print("CONTESTAR")
#salida#