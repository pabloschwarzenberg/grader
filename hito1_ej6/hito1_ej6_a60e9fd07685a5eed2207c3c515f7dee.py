#Ordenar tres números
n1=int(input("ingrese primer número"))
n2=int(input("ingrese segundo  número"))
n3=int(input("ingrese tercer número"))
a= min(n1,n2,n3)
c=max(n1,n2,n3)
b=(n1+n2+n3)- a - c
print("{},{},{}".format(a,b,c))
