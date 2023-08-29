#Ordenar tres números
x = int(print("escriba el primer numero: ")      
y = int(print("escriba el segundo numero: ")
z = int(print("escriba el tercer numero: ")

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a -c

print("los numeros ordenados son:{}, {} y {}",format(a,b,c))