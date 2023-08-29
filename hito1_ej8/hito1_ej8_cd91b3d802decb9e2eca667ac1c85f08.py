#Descomponer un número

cont=0
unidad=0
decena=0
centena=0
miles=0

while True:
  num=int(input("Ingrese un número de hasta 4 dígitos: "))
  num2=str(num)
  if(len(num2)>4):
    print("El largo del número es demasiado, intentelo de nuevo")
  else:
    break

num3=num2[::-1]

for i in num3:
  if(cont==0):
    unidad=i+"U"
    cont=1
  elif(cont==1):
    decena=i+"D"
    cont=2
  elif(cont==2):
    centena=i+"C"
    cont=3
  elif(cont==3):
    miles=i+"M"

if(len(num3)==1):
  print(unidad)
elif(len(num3)==2):
  print(decena,"+",unidad)
elif(len(num3)==3):
  print(centena,"+",decena,"+",unidad)
elif(len(num3)==4):
  print(miles,"+",centena,"+",decena,"+",unidad)
