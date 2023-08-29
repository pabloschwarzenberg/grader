#Contestador de celular
num=int(input("Ingrese número: "))
hora=int(input("Ingrese hora: "))
a=num//100000
b=num%1000
if 0<=hora<=7:
  print("Contestar")
elif 7<hora<14:
  if b==909:
    print("Contestar")
  else:
    print("No contestar")
elif 17<=hora<=19:
  if a==877:
    print("No contestar")
  else:
      print("Contestar")
elif 19<hora:
  print("No contestar")