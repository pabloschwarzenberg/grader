x1=0
x2=0
x3=0

n1=int(input("ingrese numero 1:"))
n2=int(input("ingrese numero 2:"))
n3=int(input("ingrese numero 3:"))

if (n1>=n2 and n1>=n3):
    x3=n1
    x1=n2
    x2=n3
elif (n2>=n1 and n1>=n3):
    x3=n2
    x2=n1
    x1=n3
elif (n3>=n1 and n1>=n2):
    x3=n3
    x2=n1
    x1=n2
elif (n3>=n2 and n2>=n1):
    x3=n3
    x2=n2
    x1=n1
elif (n1>=n3 and n3>=n2):
    x3=n1
    x2=n3
    x1=n2
elif (n2>=n3 and n3>=n1):
    x3=n2
    x2=n3
    x1=n1

print(str(x1)+","+str(x2)+","+ str(x3))