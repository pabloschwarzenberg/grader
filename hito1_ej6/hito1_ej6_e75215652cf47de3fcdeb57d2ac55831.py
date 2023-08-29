#Ordenar tres números
n1=int(input("inserte el primer numero"))
n2=int(input("inserte el segundo numero"))
n3=int(input("inserte el tercer numero"))
a=min(n1,n2,n3)
c=max(n1,n2,n3)
b=(n1+n2+n3)-a-c
print("{},{},{}".format(a, b, c))     