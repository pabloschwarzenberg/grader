#Contestador de celular
NU = int(input("Ingrese numero telefonico:"))
HO = int(input("Ingrese hora de la llamada:"))

if HO >= 0 and HO <= 7:
  print("CONTESTAR")

if HO > 14 and NU == 909:
  print("CONTESTAR")
  if HO > 14 and NU > 909 or NU < 909:
    print("NO CONTESTAR")
      elif HO >= 17 and HO <= 19 and NU > 877 and NU < 877:
          print("CONTESTAR")
      elif HO >= 17 and HO <= 19 and NU == 877:
          print("NO CONTESTAR")
      elif HO > 19 
          print("NO CONTESTAR")
      else:
          print("ERROR")