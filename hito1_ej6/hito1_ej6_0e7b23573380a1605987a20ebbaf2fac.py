#Ordenar tres números
n1= eval(input("Ingrese el primer numero: "))
n2= eval(input("Ingrese el segundo numero: "))
n3= eval(input("Ingrese el tercer numero: "))

a= max(n1,n2,n3)
b= min(n1,n2,n3)
c= (n1 + n2 + n3) - a - b

print("{},{},{}".format(b,c,a))