#Contestador de celular
x=input("ingrese un numero de telefono")
h=float(input("ingrese la hora de la llamada"))
lista=[x]
if 0<h and h<=7:
  print("contestar")
elif h<14 and h>7:
  if x[5]=="9" and x[6]=="0" and x[7]=="9":
    print("contestar")
  else:
    print("no contestar")
elif 17<h and h<19:
  if x[0]=="8" and x[1]=="7" and x[2]=="7":
    print("no contestar")
  else:
    print("contestar")
else:
  print("no contestar")
