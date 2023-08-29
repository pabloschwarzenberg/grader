n1=int(input("Escriba el primer valor: "))
n2=int(input("Escriba el segundo valor: "))
n3=int(input("Escriba el tercer valor: "))
a=min(n1,n2,n3)
c=max(n1,n2,n3)
b=(n1+n2+n3)-c-a
print(a,",",b,",",c)