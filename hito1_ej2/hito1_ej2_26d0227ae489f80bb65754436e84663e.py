numero=int(input("Ingrese el numero: "))
hora=int(input("Ingrese la hora: "))
resto=numero % 1000
cuociente=int(numero/100000)
if 0<=hora<=7:
  print("Contestar")
  
if 8<hora and hora<14 and resto==909:
  print("Contestar")
else:
  print("No contestar")
if 17<=hora<=19 and cuociente==877:
  print("No Contestar")
else:
  print("Contestar")
if hora>19:
  print("No contestar")