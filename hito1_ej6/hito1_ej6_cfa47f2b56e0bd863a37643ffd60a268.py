#Ordenar tres números
n1=int(input("ingrese el primer numero"))
n2=int(input("ingrese el segundo numero"))
n3=int(input("ingrese el tercer numero"))
if n1>=n2 and n2>=n3:
    print("{},{},{}".format(n3,n2,n1))
if n2>=n1 and n3>=n2:
    print("{},{},{}".format(n1,n2,n3))
if n3>=n2 and n2>=n1:
    print("{},{},{}".format(n1,n3,n2))
if n1>=n3 and n3>=n2:
    print("{},{},{}".format(n2,n3,n1))
if n3>=n1 and n1>=n2:
    print("{},{},{}".format(n2,n1,n3))
if n2>=n1 and n1>=n3:
    print("{},{},{}".format(n3,n1,n2))
 