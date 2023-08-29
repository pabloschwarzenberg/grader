nro = int(input("Ingrese un número telefónico de 8 cifras: "))
hora = int(input("Ingrese la hora en que se efectúa la llamada (entre 0 y 23hrs): "))
if 0 <= hora <= 7:
  print("Contestar llamada")
else:
  if 7 < hora <= 14 and nro%1000 == 909:
    print("Contestar llamada")
  elif 7 < hora <= 14:
    print("No contestar llamada")
  else:
    if 17 <= hora <= 19 and nro//100000 == 877:
      print("No contestar llamada")
    elif 17 <= hora <= 19:
      print("Contestar llamada")
    else:
      if hora > 19:
        print("No contestar")
