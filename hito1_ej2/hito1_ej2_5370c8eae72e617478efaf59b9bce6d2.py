#Contestador de celular
numerocell=0
while(numerocell<10000000 or numerocell>99999999):
 numerocell=int(input("ingrese su numero de telefono: "
))
hora=100
while hora<0 or hora>23:
  hora=int(input("hora de la llamada:  "))
 
if ((numerocell//100000==877) and (hora>17 and hora<=19)):
  print("NO CONTESTAR")

elif numerocell<10000000 or numerocell>99999999 and hora>=0 and hora<7:
 print("CONTESTAR")
elif numerocell%1000==909 and hora>=0 and hora<14:
 print("CONTESTAR")
else:
  print("NO CONTESTAR")     