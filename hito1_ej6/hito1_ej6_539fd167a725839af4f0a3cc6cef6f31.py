#Ordenar tres números
a= int(input("Ingrese el primer numero:"))
b= int(input("Ingrese el segundo numero:"))
c= int(input("Ingrese el tercer numero:"))

x = min(a, b, c)
y = max(a, b, c)
z = (a + b + c)- x - y

print(x,",", z,",",y)