#Contestador de celular
nmbr = str(input("Ingrese un numero telefonico porfavor:"))
hr = int(input("Ingrese una hora de llamada porfavor:"))
if hr > 0 and hr < 7:
  print("CONTESTAR")
if hr > 19 and hr <= 23:
  print("NO CONTESTAR")
else:
  if hr > 7 and hr < 14 and str(nmbr[-3]) == "9" and str(nmbr[-2]) == "0" and str(nmbr[-1]) == "9":
    print("CONTESTAR")
  if hr > 7 and hr < 14 and str(nmbr[-3]) != "9" and str(nmbr[-2]) != "0" and str(nmbr[-1]) != "9":
    print("NO CONTESTAR")
  if hr > 17 and hr < 19 and str(nmbr[0:1]) == "8" and str(nmbr[1:2]) == "7" and str(nmbr[2:3]) == "7":
    print("NO CONTESTAR")
  if hr > 17 and hr < 19 and str(nmbr[0:1]) != "8" and str(nmbr[1:2]) != "7" and str(nmbr[2:3]) != "7":
    print("CONTESTAR")