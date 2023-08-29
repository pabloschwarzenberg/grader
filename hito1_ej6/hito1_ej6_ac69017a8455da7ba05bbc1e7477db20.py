#Cesar Sanzana Burgos
#Ordenar tres números

n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))
print()

if(n1<=n2 and n2<=n3):
  print("Los numeros ordenados son:",n1,",",n2,",",n3)
elif(n2<=n1 and n1<=n3):
  print("Los numeros ordenados son:",n2,",",n1,",",n3)
elif(n3<=n1 and n1<=n2):
  print("Los numeros ordenados son:",n3,",",n1,",",n2)
elif(n3<=n2 and n2<=n1):
  print("Los numeros ordenados son:",n3,",",n2,",",n1)
elif(n1<=n3 and n3<=n2):
  print("Los numeros ordenados son:",n1,",",n3,",",n2)
elif(n2<=n3 and n3<=n1):
  print("Los numeros ordenados son:",n2,",",n3,",",n1)
else:
  print("Error, debe ingresar solo numeros enteros")