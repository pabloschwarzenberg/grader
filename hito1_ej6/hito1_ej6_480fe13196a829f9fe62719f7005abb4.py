
n1=input("ingrese el primer numero")
n1=int(n1)
n2=input("ingrese el segundo numero")
n2=int(n2)
n3=input("ingrese el tercer numero")
n3=int(n3)
if (n1>n2>n3)or(n1>n2==n3)or(n1==n2>n3):
    print(n3, n2, n1)
elif (n1>n3>n2)or(n1==n3>n2):
    print(n2,",", n3,",", n1)
elif (n2>n1>n3)or(n2>n1==n3)or(n2==n1>n3):
    print(n3,",", n1,",", n2)
elif (n2>n3>n1)or(n2==n3>n1):
    print(n1,",", n3,",", n2)
elif (n3>n2>n1)or(n3>n2==n1)or(n3==n2>n1):
    print(n1,",", n2,",", n3)
else:
    print(n1,",",n2,",",n3)