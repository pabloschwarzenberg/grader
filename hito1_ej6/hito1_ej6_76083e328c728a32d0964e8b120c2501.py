#Ordenar tres números
v1 = int(input("ingrese el primer numero:"))
v2 = int(input("ingrese el segundo numero:"))
v3 = int(input("ingrese el tercer numero:"))
x = min(v1, v2, v3)
y = max(v1, v2, v3)
z = (v1 + v2 + v3) - x - y 
print(x,',',z,',',y)







      