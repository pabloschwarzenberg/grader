#Ordenar tres números
n1=int(input("Ingrese el numero1 "))
n2=int(input("Ingrese el número 2 "))
n3=int(input("Ingrese el número 3 "))
if(n1<n2 and n1<n3):
  if(n2<n3):
    print (str(n1)+","+str(n2)+","+ str(n3))
  else: 
    print(str(n1)+","+ str(n3)+","+str(n2))


if(n2<n1 and n2<n3):
  if(n1<n3):
    print(str(n2)+ "," +str(n1)+ "," + str(n3))
  else:
    print(str(n2)+","+str(n3)+","+str(n1))



if(n3<n1 and n3<n2): 
  if(n1<n2):
    print(str(n3)+","+str(n1)+","+str(n2))
  else: 
    print(str(n3)+","+str(n2)+","+str(n1))

if n1<n2 and n1<n3:
  if n2<n3:
    print(str(n1))+ "," +str(n3)+ "," + str(n2)
else: 
  print (str(n1)+ "," +str(n3)+ "," +str(n2))