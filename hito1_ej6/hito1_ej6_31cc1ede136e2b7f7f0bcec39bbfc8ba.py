#Ordenar tres números
#Ordenar tres números
a = int(input("escriba el primer numero: "))
b = int(input("escriba el segundo numero: "))
c = int(input("escriba el tercer numero: "))
x = min(a,b,c)
y = max(a,b,c)
z = (a+b+c)-x-y
print("los numeros son", (x,z,y))
