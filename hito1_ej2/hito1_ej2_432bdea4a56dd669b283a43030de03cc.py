#Contestador de cel
hora=(input("Ingrese hora de la llamada: "))
tel=(input("Ingrese numero telefonico: "))
if 0<int(hora) and int(hora)<7:
  print("Resultado: CONTESTAR")
elif 7<=int(hora) and int(hora)<=13:
  if (int(tel)%1000==909):
    print("Resultado: CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif 14<=int(hora) and int(hora) <=17:
  print("Resultado: NO CONTESTAR")
elif 17<int(hora) and int(hora)<=19:
  if int(tel)//100000==877:
    print("Resultado: NO CONTESTAR")
  else:
    print("Resultado: CONTESTAR")
elif int(hora)>19:
  print("Resultado: NO CONTESTAR")