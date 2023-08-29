#Ordenar tres números
n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
n3=int(input("Ingrese el tercer número: "))

a= min(n1,n2,n3)
c= max(n1,n2,n3)
b= (n1 + n2 + n3) - a - c

print (a, ",", b, ",", c)
