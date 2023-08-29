#Ordenar tres números
n1=input("Numero 1:")
n2=input("Numero 2:")
n3=input("Numero 3:")

n1=int(n1)
n2=int(n2)
n3=int(n3)

if n1<=n2<=n3:
    print(n1,",",n2,",",n3)
elif n1<=n3<=n2:
    print(n1,",",n3,",",n2)
elif n2<=n1<=n3:
    print(n2,",",n1,",",n3)
elif n2<=n3<=n1:
    print(n2,",",n3,",",n1)
elif n3<=n1<=n2:
    print(n3,",",n1,",",n2)
elif n3<=n2<=n1:
    print(n3,",",n2,",",n1)
