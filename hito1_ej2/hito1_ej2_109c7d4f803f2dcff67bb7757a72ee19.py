lt = input("Ingrese numero telefonico: ")
hl = int(input("Ingrese la hora de llamada: "))
if 0 <= hl <= 7:
  print("Resultado: CONTESTAR")
elif hl < 14:
  if lt.endswith("909"):
    print("Resultado: CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif 17<=hl<=19:
  if lt.startswith("877"):
    print("Resultado: NO CONTESTAR")
  else: 
    print("Resultado: CONTESTAR")
elif 19<hl:
  print("Resultado: NO CONTESTAR")