#Ordenar tres números
a = eval(input("Numero 1: "))
b = eval(input("Numero 2: "))
c = eval(input("Numero 3: "))

x = max(a,b,c)
y = min(a,b,c)
z = a + b + c - x - y

print("Los números ordenados de menor a mayor son: ",y,",",z,",",x)