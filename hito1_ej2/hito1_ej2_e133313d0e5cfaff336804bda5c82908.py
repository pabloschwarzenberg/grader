#Contestador de celular
no=int(input("ingrese un numero de ocho cifras" ))
hr=int(input("ingrese la hora" ))
x1=(no//1000)*1000
x2=(no//100000)
z=no-x1
if 0<=hr<=7:
  print("CONTESTAR")
elif(17<=hr<=19 and x2!=877):
  print("CONTESTAR")
elif(17<=hr<=19 and x2==877):
  print("NO CONTESTAR")
elif(hr<14 and z!=909):
  print("NO CONTESTAR")
elif(hr<14 and z==909):
  print("CONTESTAR")
elif hr>19:
  print("NO CONTESTAR")