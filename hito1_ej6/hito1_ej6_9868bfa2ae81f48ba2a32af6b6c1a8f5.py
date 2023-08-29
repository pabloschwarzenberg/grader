#Ordenar tres números
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un segundo numero: "))
z = int(input("ingrese el tercer numero: "))

ma = max(x,y,z)
mi = min(x,y,z)
med = (x+y+z)-(mi+ma)

print(mi,",",med,",",ma)