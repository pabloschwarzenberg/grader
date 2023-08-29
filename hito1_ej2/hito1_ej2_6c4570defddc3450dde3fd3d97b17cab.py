#Contestador de celular
nume = str(input("Ingrese numero telefonico:"))

hr = int(input("Ingrese hora de la llamada:"))

if hr > 0 and hr < 7:

  print("CONTESTAR")

if hr > 19 and hr <= 23:

  print("NO CONTESTAR")

else:

  if hr > 7 and hr < 14 and str(nume[-3]) == "9" and str(nume[-2]) == "0" and str(nume[-1]) == "9":

    print("CONTESTAR")

  if hr > 7 and hr < 14 and str(nume[-3]) != "9" and str(nume[-2]) != "0" and str(nume[-1]) != "9":

    print("NO CONTESTAR")

  if hr > 17 and hr < 19 and str(nume[0:1]) == "8" and str(nume[1:2]) == "7" and str(nume[2:3]) == "7":

    print("NO CONTESTAR")

  if hr > 17 and hr < 19 and str(nume[0:1]) != "8" and str(nume[1:2]) != "7" and str(nume[2:3]) != "7":

    print("CONTESTAR")      