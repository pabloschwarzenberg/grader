#Ordenar tres números
n1= int(input("ingrese un numero: "))
n2= int(input("ingrese otro numero: "))
n3= int(input("ingrese el ultimo numero: "))
if (n1<=n2<=n3):
  print("el orden de menor a mayor es: ",n1,",",n2,",",n3)
if (n2<=n1<=n3):
  print("el orden de menor a mayor es: ",n2,",",n1,",",n3)
if (n3<=n2<=n1):
  print("el orden de menor a mayor es: ",n3,",",n2,",",n1)
if (n3<=n1<=n2):
  print("el orden de menor a mayor es: ",n3,",",n1,",",n2)
if (n1<=n3<=n2):
  print("el orden de menor a mayor es: ",n1,",",n3,",",n2)
if (n2<=n3<=n1):
  print("el orden de menor a mayor es: ",n2,",",n3,",",n1)