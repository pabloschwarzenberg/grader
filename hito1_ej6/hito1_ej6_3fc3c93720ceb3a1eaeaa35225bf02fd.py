n=int(input("Ingrese numero 1 : "))
n2=int(input("Ingrese numero 2 : "))
n3=int(input("Ingrese numero 3 : "))

if n<=n2<=n3:
  print(n,",",n2,",",n3)
elif n<=n3<=n2:
  print(n,",",n3,",",n2)
elif n2<=n<=n3:
  print(n2,",",n,",",n3)
elif n2<=n3<=n:
  print(n2,",",n3,",",n)
elif n3<=n<=n2:
  print(n3,",",n,",",n2)
elif n3<=n2<=n:
  print(n3,",",n2,",",n)   
