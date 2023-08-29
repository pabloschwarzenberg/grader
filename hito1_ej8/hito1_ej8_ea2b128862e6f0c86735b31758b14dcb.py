#Descomponer un número
n=int(input("Ingrese un numero: "))

n1=str(n)

if (0<=n<=9):
    n11=n1[0:1]
    n111=int(n11)
    print("%dU" %n111)
elif(10<=n<=99):
    n11=n1[0:1]
    n111=int(n11)
    n22=n1[1:2]
    n222=int(n22)
    print("%dD + %dU" %(n111,n222))
elif(100<=n<=999):
    n11=n1[0:1]
    n111=int(n11)
    n22=n1[1:2]
    n222=int(n22)
    n33=n1[2:3]
    n333=int(n33)
    print("%dC + %dD + %dU"%(n111,n222,n333))
elif(1000<=n<=9999):
    n11=n1[0:1]
    n111=int(n11)
    n22=n1[1:2]
    n222=int(n22)
    n33=n1[2:3]
    n333=int(n33)
    n44=n1[3:4]
    n444=int(n44)
    print("%dM + %dC + %dD + %dU"%(n111,n222,n333,n444))
else:
    print("----ERROR----")