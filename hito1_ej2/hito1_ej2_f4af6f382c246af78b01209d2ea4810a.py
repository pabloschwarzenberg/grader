#Contestador de celular
ph_number = int(input("Ingrese numero telefonico"))
hour = int(input("Ingrese hora de la llamada"))

if 0 <= hour <= 7:
  print("CONTESTAR")
elif 7 < hour < 14:
  if ph_number % 1000 == 909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif 17 <= hour <= 19:
  if int(str(ph_number)[::-1]) % 1000 == 778:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
else:
  print("NO CONTESTAR")