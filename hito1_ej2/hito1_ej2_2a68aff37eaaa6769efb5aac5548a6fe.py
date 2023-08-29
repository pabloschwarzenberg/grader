telefono=int(input("Ingrese numero de telefono"))
hora=int(input("Ingrese hora actual entre 0 y 23"))

if 10000000 <= telefono <= 99999999 and 0 <= hora <= 23:
  if 0 <= hora <= 7:
    print("CONTESTAR")
  if 8 <= hora <=14:
    u = telefono % 1000
    if u == 909:
      print("CONTESTAR")
    else:
      print("NO CONTESTAR")
  if 15 <= hora <= 16:
    print("CONTESTAR")
  if 17 <= hora <= 19:
    p = telefono // 100000
    if p == 877:
      print("NO CONTESTAR")
    else:
      print("CONTESTAR")
  if 20 <= hora <= 23:
    print("NO CONTESTAR") 



else:
  print("telefono o hora incorrecta")