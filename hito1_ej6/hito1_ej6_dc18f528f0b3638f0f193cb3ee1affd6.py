#Ordenar tres números
a = int(input("escriba el primer numero:"))      
b = int(input("escriba el segundo numero:"))   
c = int(input("escriba el tercer numero:"))   

x = min(a, b, c)
z = max(a, b, c)
y = (a + b + c) - x - z

print("los numeros ordenados son: {}, {}, {}" .format(x, y, z))