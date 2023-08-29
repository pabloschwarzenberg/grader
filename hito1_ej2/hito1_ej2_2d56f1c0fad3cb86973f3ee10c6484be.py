#Contestador de celular
n=int(input("Ingrese hora de la llamada:"))
h=int(input("Ingrese numero de 8 digitos:"))    
if 0<=h<=7:
   print("CONTESTAR")
elif 7<h<14 and n%1000==909:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")
if 14<h<17 and format(n/10000,0)==877:
    print("CONTESTAR")
elif 17<=h<=19:
    print("CONTESTAR")
if 19<h:
   print("NO CONTESTAR")
    
    
