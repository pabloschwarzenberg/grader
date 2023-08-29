#Ordenar tres números
x = int(input("Escriba el primer numero: "))
y = int(input("Escriba el segundo numero: "))
z = int(input("Escriba el tercer numero: "))

q = max(x,y,z)
print("el numero mayor es: ", q)
w = min(x,y,z)
print("el numero menor es: ", w)

e = (x + y + z) - q - w

print("Los números ordenados de mayor a menor son: ", w ," , ", e ," , ", q)
   