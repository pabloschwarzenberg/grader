#INGRESAR NÚMEROS
n1=int(input("Ingresa el 1er número: "))
n2=int(input("Ingresa el 2do número: "))
n3=int(input("Ingresa el 3er número: "))
#ORDEN
if n1>=n2>=n3:
  print(n3,",",n2,",",n1)
elif n1>=n3>=n2:
  print(n2,",",n3,",",n1)
elif n2>=n1>=n3:
  print(n3,",",n1,",",n2)
elif n2>=n3>=n1:
  print(n1,",",n3,",",n2)
elif n3>=n2>=n1:
  print(n1,",",n2,",",n3)
else:
  print(n2,",",n1,",",n3)