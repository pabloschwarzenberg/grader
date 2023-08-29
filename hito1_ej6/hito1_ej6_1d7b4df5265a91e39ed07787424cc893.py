  #Ordenar tres números
#ENTRADA
x = int(input("ingrese el primer numero "))
y = int(input("ingrese el segundo numero "))
z = int(input("ingrese el tercer numero "))
ma = max(x,y,z)
mi = min(x,y,z) 
d = (x + y + z) - ma - mi
print(mi ," , ", d ,", ",ma)