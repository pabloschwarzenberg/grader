#Ordenar tres números
a = int(input("ingrese un numero:"))
b = int(input("ingrese un segundo numero:"))
c = int(input("ingrese un tercer numero:"))
ma = max(a, b, c)
mi = min(a, b, c)
me = (a + b + c) - ma - mi 
print(mi ,",", me, ",", ma)     