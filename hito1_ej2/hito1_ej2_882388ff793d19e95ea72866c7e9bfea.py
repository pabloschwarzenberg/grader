numero=eval(input("ingrese un numero telefonico:"))
hora=eval(input("ingrese la hora:"))

if(hora>=0  and hora<=7):
  print("Contestar")
elif(hora<14 and numero%1000==909):
  print("Contestar")
elif(hora>=17 and hora<=19 and not(numero//100000==877)):
  print("Contestar")
else:
  print("No contestar")