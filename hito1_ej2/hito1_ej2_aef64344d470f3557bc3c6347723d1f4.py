#Contestador de celular
a=int(input("Ingrese el numero:"))
b=int(input("Ingrese la hora:"))

if 0<=b<=7:
  print("CONTESTA")
elif 8<=b<=14:
  if a%1000==909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif 17<=b<=19:
  if a//100000==877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif 20<=b<=23:
  print("NO CONTESTAR")