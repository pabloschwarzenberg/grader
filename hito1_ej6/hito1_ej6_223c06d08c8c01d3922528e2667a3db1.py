#Ordenar tres números
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
d = max(a,b,c)
e = min(a,b,c)
f = (a + b + c)- e - d
print(e,",", f, ",", d)