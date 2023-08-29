#Ordenar tres números
a = int(input("Ingrese un primer numero: "))
b = int(input("Ingrese un segundo numero: "))
c = int(input("Ingrese un tercer numero: "))

z = max(a,b,c)
x = min(a,b,c)

s = (a+b+c-z-x)

print(x,",",s,",",z)