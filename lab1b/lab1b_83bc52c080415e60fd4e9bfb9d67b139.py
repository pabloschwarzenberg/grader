#Heladas
s1=int(input("temperatura zona 1:"))
print("la temperatura de la zona 1 es:"+str(s1))
s2=int(input("temperatura zona 2 es: "))
print ("la temperatura de la zona 2 es: "+str(s2))
s3=int(input("temperatura zona 3 es: "))
print ("la temperatura de la zona 3 es: "+str(s3))
if((s1<=0) or (s2<=0) or (s3<=0)):
  print("encendido\n"*3)

else:
  
  if (s1<=5):
    print('encendido')
  else:
    print('apagado')

  if (s2<=5):
    print('encendido')
  else:
    print('apagado')
  if (s3<=5):
    print('encendido')
  else:
    print('apagado')