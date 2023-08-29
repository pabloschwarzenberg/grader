#Contestador de celular
#definimos h=hora y c=celular
#iniciamos por la restriccion mas simple que es de 19 a 23h
c=int(input("Ingrese su numero telefonico: "))
h=int(input("Ingrese hora de la llamada: "))
#d para ult tres digitos de c
d=int(c*0.00001)
aux=int(int(c*0.001)*1000)
e=int(c-aux)

if(19<h<=23):
  print("Resultado: NO CONTESTAR")

elif(0<=h<=7):
  print("Resultado: CONTESTAR")
  
elif(8<=h<14 and e==909):
  print("Resultado: CONTESTAR")
  
elif(8<=h<14 and e!=909):
  print("Resultado: NO CONTESTAR")
  
elif(14<h<17):
  print("Resultado: NO CONTESTAR")
  
elif(15<=h<=19 and d!=877):
  print("Resultado: CONTESTAR")

elif(15<=h<=19 and d==877):
  print("Resultado: NO CONTESTAR")
  