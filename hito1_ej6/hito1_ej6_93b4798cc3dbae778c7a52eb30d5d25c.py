#Ordenar tres números
n1=int(input("Numero uno:"))
n2=int(input("Numero dos:"))
n3=int(input("Numero tres:"))

if n1>=n2>=n3: print(n3,",",n2,",",n1)

if n1>=n3>n2: print(n2,",",n3,",",n1)

if n3>n1>n2: print(n2,",",n1,",",n3)

if n3>=n2>=n1: print(n1,",",n2,",",n3)

if n2>n1>=n3: print(n3,",",n1,",",n2)

if n2>n3>n1: print(n1,",",n3,",",n2)