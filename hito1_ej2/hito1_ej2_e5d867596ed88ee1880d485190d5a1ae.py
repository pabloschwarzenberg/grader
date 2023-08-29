#ENTRADA
numero_telefonico=int(input("Ingrese el numero telefonico: "))
hora_del_dia=int(input("Ingrese una hora del dia: "))

#DESARROLLO
if len(str(numero_telefonico)) > 8:
  print("Numero Invalido")
else:
  if hora_del_dia >=0 and hora_del_dia <=7:
    print("CONTESTAR")
  elif hora_del_dia < 14 and str(numero_telefonico)[5:] == "909":
    print("CONTESTAR")
  elif hora_del_dia < 14 and str(numero_telefonico)[5:] != "909":
      print("NO CONTESTAR")   
  elif hora_del_dia >=17 and hora_del_dia <=19 and str(numero_telefonico)[:3] != "877":
    print("CONTESTAR")
  elif hora_del_dia >=17 and hora_del_dia <=19 and str(numero_telefonico)[:3] == "877":
    print("NO CONTESTAR")
  elif hora_del_dia > 13 and hora_del_dia < 17:
      print("NO CONTESTAR")
  if hora_del_dia > 19:
    print("NO CONTESTAR")
      