#Ordenar tres números
n1 = int(input("ingrese un primer numero: "))
n2 = int(input("ingrese un segundo numero: "))
n3 = int(input("ingrese un tercer numero: "))

a = max(n1,n2,n3)
b = min(n1,n2,n3)
c = n1 + n2 + n3 - a -b
print(b,",",c,",",a)