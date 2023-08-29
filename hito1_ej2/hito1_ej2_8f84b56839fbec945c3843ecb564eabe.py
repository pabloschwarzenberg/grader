#Contestador de celular
celular= int(input("ingrese celular "))
h=int(input("ingrese h "))
termina909=int(celular%1000)
comienza877=int(celular//100000)
if(celular>99999999)and(celular<10000000):
  print("celular fuera de area")
elif(h<=0)and(h>=23):
  print("hora fuera de area")
elif(h>=0)and(h<=7):
  print("CONTESTAR")
elif(h<14)and(h>7):
  if termina909==909:
      print("CONTESTAR")
  else:
      print("NO CONTESTAR")
elif(h<=19)and(h>=17):
  if comienza877==877:
      print("NO CONTESTAR")
  else:
      print("CONTESTAR")
elif(h>19):
  print("NO CONTESTAR")      