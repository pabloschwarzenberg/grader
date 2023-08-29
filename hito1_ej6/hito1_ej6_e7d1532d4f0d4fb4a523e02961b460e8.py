#Ordenar tres números
numero1=int(input("Ingrese el número 1 "))
numero2=int(input("Ingrese el número 2 "))
numero3=int(input("Ingrese el número 3 "))
if(numero1<numero2 and numero1<numero3):#8,4,3
  if(numero2<numero3):#4,3
    print (str(numero1)+","+str(numero2)+","+ str(numero3))
  else: #4,6
    print(str(numero1)+","+ str(numero3)+","+str(numero2))


if(numero2<numero1 and numero2<numero3):#4,8,2
  if(numero1<numero3):
    print(str(numero2)+ "," +str(numero1)+ "," + str(numero3))
  else:#2,8,4
    print(str(numero2)+","+str(numero3)+","+str(numero1))



if(numero3<numero1 and numero3<numero2): #8,4,10
  if(numero1<numero2):
    print(str(numero3)+","+str(numero1)+","+str(numero2))
  else: #4,6,8
    print(str(numero3)+","+str(numero2)+","+str(numero1))

if numero1<numero2 and numero1<numero3:
  if numero2<numero3:
    print(str(numero1))+ "," +str(numero3)+ "," + str(numero2)
else: #8, 4, 4
  print (str(numero1)+ "," +str(numero3)+ "," +str(numero2))