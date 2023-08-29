#Entrada
teléfono = int(input("Ingrese el número telefónico :"))
hora = int(input("Ingrese hora de la llamada (AM) :"))
#Procesamiento, Salida
if 7 >= hora >= 0:
  print("CONTESTAR")
elif 14 > hora and teléfono == 77389909:
  print("CONTESTAR")
elif 14 > hora:
  print("NO CONTESTAR")
elif 19 >= hora >= 17 and teléfono == 87765545:
  print("NO CONTESTAR")
elif 19 >= hora >= 17:
  print("CONTESTAR")
else:
  if 19 < hora:
    print("NO CONTESTAR")
  