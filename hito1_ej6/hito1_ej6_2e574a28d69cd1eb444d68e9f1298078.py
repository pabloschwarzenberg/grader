#Ordenar tres números
a = int(input("Escriba el primer numero: "))
b = int(input("Escriba el segundo numero: "))
c = int(input("Escriba el tercer numero: "))

x = min(a,b,c)
y = max(a,b,c)
z = (a+b+c)-x-y

print("los numeros son", (x,z,y))