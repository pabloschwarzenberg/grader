#Ordenar tres números
print("Ordenaremos los numeros de menor a mayor")
n1= eval(input("ingresa el primer numero: "))
n2= eval(input("ingresa el segundo numero: "))
n3= eval(input("ingresa el tercer numero: "))
if n1<=n2<=n3:
  print("Orden de menor a mayor:",n1,",",n2,",",n3)
elif n2<=n3<=n1:
  print("Orden de menor a mayor",n2,",",n3,",",n1)
elif n3<=n1<=n2:
  print("Orden de menor a mayor",n3,",",n1,",",n2)
elif n3>=n1>=n2:
 print("Orden de menor a mayor",n2,",",n1,",",n3)