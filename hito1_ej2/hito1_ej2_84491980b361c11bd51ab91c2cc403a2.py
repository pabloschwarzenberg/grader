#Contestador de celular
n=int(input("ingrese numero telefonico:"))
if(n>9999999 and n<100000000):
  pass
else:
   (print("este no es un telefono valido"))
h=int(input("ingrese la hora de la llamada:"))
if(h>=24 and h<0):
  print("error esa hora no existe")
if(h<=7):
  print("Contestar ya que puede ser una emergencia")
if(h<14 and h>7):
  if(n%1000==909):
   print("Contestar")
   if(n%1000!=909):
    print("No contestar")
  
if(h>=17 and h<=19):
  if(n>=87700000 and n<=87799999):
   print("No contestar")
  if (n>87799999 or n<87700000):
    print("Contestar")
elif(h>19):
  print("No contestar")   