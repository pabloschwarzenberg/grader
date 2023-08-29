#Ordenar tres números
n1=int(input("Ingresa el primer numero: "))
n2=int(input("Ingresa el segundo numero: "))
n3=int(input("Ingresa el tercer numero: "))
a=min(n1,n2,n3)
b=max(n1,n2,n3)
c=(n1+n2+n3)-a-b
print(a,",",c,",",b)         