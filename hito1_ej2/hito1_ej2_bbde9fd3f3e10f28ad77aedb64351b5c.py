#Contestador de celular
telefono = int(input("Ingrese un numero telefonico: "))
hora = int(input("Ingrese la hora de la llamada: "))
if telefono<100000000:
  if hora == 0 or hora ==1 or hora == 2 or hora == 3 or hora == 4 or hora == 5 or hora == 6 or hora == 7:
    if hora != [8,23]:
      print("CONTESTAR")
    else:
      print("NO CONTESTAR")
  if hora == 8 or hora == 9 or hora ==10 or hora == 11 or hora == 12 or hora == 13:
      CENTENAS = ((telefono%1000 - telefono%100)//100)
      DECENAS = ((telefono%100 - telefono%10)//10)
      UNIDAD = (telefono%10)
      if CENTENAS == 9 and DECENAS == 0 and UNIDAD == 9:
        print("CONTESTAR")
      else:
        print("NO CONTESTAR")
  if hora == 17 or hora == 18 or hora == 19:
      DMILLON = ((telefono%100000000 - telefono%10000000)//10000000)
      UMILLON = ((telefono%10000000 - telefono%1000000)//1000000)
      CMIL = ((telefono%1000000 - telefono%100000)//100000)
      if DMILLON == 8 and UMILLON == 7 and CMIL == 7:
        print("NO CONTESTAR")
      else:
        print("CONTESTAR")
  if hora == 20 or hora == 21 or hora == 22 or hora == 23:
      print("NO CONTESTAR")