n1=input("N°1: ")
n2=input("N°2: ")
n3=input("N°3: ")

n1=int(n1)
n2=int(n2)
n3=int(n3)

if (n1<=n2<=n3):
    print(n1,",", n2,",", n3)

if (n1<=n3<=n2):
    print(n1,",", n3,",", n2)

if (n2<=n1<=n3):
    print(n2,",", n1,",", n3)

if (n2<=n3<=n1):
    print(n2,",", n3,",", n1)

if (n3<=n2<=n1):
    print(n3,",", n2,",", n1)

if (n3<=n1<=n2):
    print(n3,",", n1,",", n2)

