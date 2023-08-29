#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("ingrese hora: "))

if hora:
  if (hora>=0) and (hora<=7):
    print("contestar")
  elif hora:
    if (hora>=7) and (hora<=14) and (numero %1000 == 909):
      print("contestar")
    else:
      print("no contestar")
  elif hora:
      if hora>=17 and hora <=19 or numero//1000 == 877:
        print("contestar")
      else:
        print("no contestar")
  else:
        hora>=20 and hora<=24
        print("no contestar")