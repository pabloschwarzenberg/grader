N = str(input("Ingrese numero telefonico:"))
H = int(input("Ingrese hora de la llamada:"))
if H > 0 and H < 7:
  print("CONTESTAR")
if H > 19 and H <= 23:
  print("NO CONTESTAR")
else:
  if H > 7 and H < 14 and str(N[-3]) == "9" and str(N[-2]) == "0" and str(N[-1]) == "9":
    print("CONTESTAR")
  if H > 7 and H < 14 and str(N[-3]) != "9" and str(N[-2]) != "0" and str(N[-1]) != "9":
    print("NO CONTESTAR")
  if H > 17 and H < 19 and str(N[0:1]) == "8" and str(N[1:2]) == "7" and str(N[2:3]) == "7":
    print("NO CONTESTAR")
  if H > 17 and H < 19 and str(N[0:1]) != "8" and str(N[1:2]) != "7" and str(N[2:3]) != "7":
    print("CONTESTAR")

      