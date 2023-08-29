#Ordenar tres números
n1=int(input("ingrese un numero: "))
n2=int(input("ingrese un numero: "))
n3=int(input("ingrese un numero: "))
a1=min(n1,n2,n3)
a2=max(n1,n2,n3)
a3=(n1+n2+n3)-a1-a2
print('{} , {} , {}'.format(a1,a3,a2))    