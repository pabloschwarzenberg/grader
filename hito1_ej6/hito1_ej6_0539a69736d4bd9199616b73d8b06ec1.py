#Ordenar tres números
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un segundo numero: "))
c = int(input("Ingrese un tercer numero: "))
g = max(a,b,c)
h = min(a,b,c)
d = (a + b + c) - g - h
print("De menor a mayor es ", h ," , ", d , " , ", g)