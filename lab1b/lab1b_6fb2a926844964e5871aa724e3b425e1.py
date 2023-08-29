#Heladas
sensor1=int(input("ingrese valor:"))
sensor2=int(input("ingrese valor:"))
sensor3=int(input("ingrese valor:"))

if ((sensor1<=0) or (sensor2<=0) or (sensor3<=0)):
  print("encendido\n"*3)
else:


  if (sensor1<=5):
    print("encendido")
  else:
    print("apagado")


  if (sensor2<=5):
    print("encendido")
  else:
    print("apagado")


  if (sensor3<=5):
    print("encendido")
  else:
    print("apagado")   