#Contestador de celular
num = str(input("Ingrese numero de telefonico:"))

hr = int(input("Ingrese hora de la llamada:"))

if hr > 0 and hr < 7:

  print("CONTESTAR")

if hr > 19 and hr <= 23:

  print("NO CONTESTAR")

else:

  if hr > 7 and hr < 14 and str(num[-3]) == "9" and str(num[-2]) == "0" and str(num[-1]) == "9":

    print("CONTESTAR")

  if hr > 7 and hr < 14 and str(num[-3]) != "9" and str(num[-2]) != "0" and str(num[-1]) != "9":

    print("NO CONTESTAR")

  if hr > 17 and hr < 19 and str(num[0:1]) == "8" and str(num[1:2]) == "7" and str(num[2:3]) == "7":

    print("NO CONTESTAR")

  if hr > 17 and hr < 19 and str(num[0:1]) != "8" and str(num[1:2]) != "7" and str(num[2:3]) != "7":

    print("CONTESTAR")