n1=eval(input("ingrese un numero: "))
n2=eval(input("ingrese un numero: "))
n3=eval(input("ingrese un numero: "))
if n1<=n2 and n2<=n3:
  print(n1,",",n2,",",n3)
if n2<=n1 and n1<=n3:
  print(n2,",",n1,",",n3)
if n3<=n1 and n1<=n2:
  print(n3,",",n1,",",n2)
if n1<=n3 and n3<=n2:
  print(n1,",",n3,",",n2)
if n3<=n2 and n2<=n1:
  print(n3,",",n2,",",n1)
if n2<=n3 and n3<=n1:
  print(n2,",",n3,",",n1)  
