#Contestador de celular
nt=int(input("ingrese numero telefonico de 8 digitos:"))
hl=int(input("ingrese hora de la llamada:"))
if 0<=hl<=7:
  print("CONTESTAR")
elif 7<hl<14 and nt%1000==909:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")
if 14<hl<17 and format(nt/10000,0)==877:
  print("CONTESTAR")
elif 17<=hl<=19:
  print("CONTESTAR")
if hl>19:
  print("NO CONTESTAR")