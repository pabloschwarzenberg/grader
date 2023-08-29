#Ordenar tres números
n1=int(input("ingrese el primer número:"))
n2=int(input("ingrese el segundo número:"))
n3=int(input("ingrese el tercer número:"))
if n1<=n2 and n1<=n3:
  if n2<=n3:
    print(n1,",",n2,",",n3)
  else:
    print(n1,",",n3,",",n2)
elif n2<=n1 and n2<=n3:
  if n1<=n3:
    print(n2,",",n1,",",n3)
  else:
    print(n2,",",n3,",",n1)
else:
   if n2<=n1:
     print(n3,",",n2,",",n1)
   else:
     print(n3,",",n1,",",n2)