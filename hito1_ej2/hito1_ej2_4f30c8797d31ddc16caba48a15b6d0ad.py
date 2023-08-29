#Contestador de celular
a=int(input("ingrese numero de telefono: "))
b=int(input("ingrese hora de la llamada: "))

if(0<b<7):
  c=contestar

if(8<b<14):
  respu=a%1000
  elif(respu==909):
    c=contestar
  else:
    c=no contestar

if(15<=b<=16):
  c=no contestar

if(17<b<=19):
  if(87700000<=a<87800000):
    c=contestar
  else:
    c=no contestar

if(b>19):
  c=no contestar
print("resultado", c)

if(9999999<a<100000000):
  print("numero invalido")
if(b<0) or (b>23):
  print("hora invalida")

print(c)