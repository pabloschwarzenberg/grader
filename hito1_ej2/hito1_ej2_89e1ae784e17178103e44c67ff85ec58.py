#Contestador de celular
n=int(input("Ingrese un numero telefonico: "))
hora=int(input("Ingrese hora de llamada: "))
assert 0<=hora<=23
if 0<hora<7:
  print("CONTESTAR")
elif 7<=hora<14:
  if n % 1000 == 909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif 17<=hora<=19:
  if n//100000==877:
   print("NO CONTESTAR")
  else:
   print("CONTESTAR")
if 19<hora<=23:
  print("NO CONTESTAR")