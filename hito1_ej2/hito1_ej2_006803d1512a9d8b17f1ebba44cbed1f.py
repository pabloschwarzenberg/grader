#Contestador de celular
numero=input("Ingrese su numero de telefono: ")
hora=int(input("Ingrese la hora: "))
f1=eval(numero[7])
f2=eval(numero[6])
f3=eval(numero[5])
i1=eval(numero[0])
i2=eval(numero[1])
i3=eval(numero[2])
if(hora>=0 and hora<=7):
  print("Contestar")
elif(hora>=8 and hora<=14 and f1==9 and f2==0 and f3==9):
  print("Contestar")
elif(hora>=8 and hora<=14):
  print("No contestar")
elif(hora>=17 and hora<=19 and i1==8 and i2==7 and i3==7):
  print("No contestar")
elif(hora>=17 and hora<=19):
  print("Contestar")
elif(hora>=19 and hora<=23):
  print("No contestar")