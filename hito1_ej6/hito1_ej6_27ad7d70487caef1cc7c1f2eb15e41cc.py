#Ordenar tres númer0
n1=eval(input("ingrese un numero "))
n2=eval(input("ingrese un numero "))
n3=eval(input("ingrese un numero "))
if(n1<=n2<=n3):
  print("numero de menor a mayor",n1,",",n2,",",n3)
if(n2<=n3<=n1):
  print("numero de menor a mayor",n2,",",n3,",",n1)
if(n3<=n1<=n2):
  print("numero de menor a mayor",n3,",",n1,",",n2)
if(n3<=n2<=n1):
  print("numero de menor a mayor",n3,",",n2,",",n1)
if(n1<=n3<=n2):
  print("numero de menor a mayor",n1,",",n3,",",n2)
if(n2<=n1<=n3):
  print("numero de menor a mayor",n2,",",n1,",",n3)