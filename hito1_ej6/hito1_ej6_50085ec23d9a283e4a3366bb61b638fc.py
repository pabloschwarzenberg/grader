n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))
n3=int(input("Numero 3: "))

if (n1<=n2<=n3):
    print(n1,",", n2,",", n3)

elif (n1<=n3<=n2):
    print(n1,",", n3,",", n2)

elif (n2<=n1<=n3):
    print(n2,",", n1,",", n3)

elif (n2<=n3<=n1):
    print(n2,",", n3,",", n1)

elif (n3<=n1<=n2):
    print(n3,",", n1,",", n2)

elif (n3<=n2<=n3):
    print(n3,",", n2,",", n3)