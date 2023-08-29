#Contestador de celular
#Contestador de celular
#definimos las variables
x=int(input("ingrese el numero de celular: "))
h=int(input("ingrese la hora en la que llamó: "))
#imprimimos los resultados con sus condiciones
if h >= 0 and h <= 7:
  print("CONTESTAR")
elif h >= 17 and h <= 19 and x // 1000000 == 877:
  print("CONTESTAR")
elif h <14 or x % 100 == 909:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")
