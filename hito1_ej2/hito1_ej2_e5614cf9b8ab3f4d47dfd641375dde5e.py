#Contestador de celular
n = eval(input("ingrese un numero de telefono de 8 digitos: "))
h = eval(input("ingrese un hora de 0 a 23: "))
numero = 77389909
numero_2 = 87745789
if 0<h<7:
  print("es urgente")
elif n == numero:
  print("contestar")

elif 7<h<14:
  print("contestar")


elif n == numero_2:
  print("contestar")

elif 17<h<19:
  print("no contestar")
elif h >= 20 and h<=23:
  print("no contestar")
  