#Contestador de celular
l=[]
numero=input("escribir el numero de telefono")
hora=int(input("escribir la hora"))

if hora>=0 and hora<=7:
  print("CONTESTAR")
  
if hora<14 and numero[-1]=="9" and numero[-2]=="0" and numero[-3]=="9":
  print("CONTESTAR")
  
if hora>=17 and hora<19:
  if numero[0]=="8" and numero[1]=="7" and numero[2]=="7":
    print(" NO CONTESTAR")
  else:
    print("CONTESTAR")

if hora>=19:
  print("NO CONTESTAR")
