#Contestador de celular
a=int(input("ingrese numero de telefono de 8 cifras:"))
b=int(input("ingrese hora de la llamada:"))
if 10000000<= a<=99999999 and 0<=b<=23:
  if 0<=b<=7:
    print("resultado:contestar")
  if 7<b<=14 and a%1000!=909:
    print("resulatdo:no contestar")
  if a%1000==909 and 7<b<=14:
    print("resultado:contestar")
  else:
    print("resulado:no contestar")
  if 15<=b<17:
    print("resultado:no contestar")
  if 17<=b<=19:
    print("resultado:contestar")
    if a//100000==877:
      print("resultado:no contestar")
    else:
      print("resultado:contestar")
  if 19<b<=23:
    print("resultado:no contestar")
else:
  print("uno o mas datos ingresados es incorrecto")