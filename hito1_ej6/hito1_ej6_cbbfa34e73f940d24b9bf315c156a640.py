#Ordenar tres números
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if n1>n2>n3:
    print(n3,n2,n1,sep=",")
elif n1<n2<n3:
    print(n1,n2,n3,sep=",")
elif n2<n3<n1:
    print(n2,n3,n1,sep=",")
elif n3>n1>n2:
    print(n2,n1,n3,sep=",")
elif n2>n1>n3:
    print(n3,n1,n2,sep=",")
elif n2>n3>n1:
    print(n1,n3,n2,sep=",")
elif n2==n3>n1:
    print(n1,n3,n2,sep=",")
elif n2==n3<n1:
    print(n3,n2,n1,sep=",")
elif n2<n3==n1:
    print(n2,n3,n1,sep=",")
elif n2>n3==n1:
    print(n3,n1,n2,sep=",")
elif n2==n1>n3:
    print(n3,n1,n2,sep=",")
elif n2==n1<n3:
    print(n1,n2,n3,sep=",")
else:
    print(n1,n2,n3,sep=",")      