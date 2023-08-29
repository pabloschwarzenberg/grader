#Ordenar tres números
x = int(input("Escriba el primer numero: "))
y = int(input("Escriba el segundo numero: "))
z = int(input("Escriba el tercer numero: "))
a = min(x , y , z)
c = max(x , y , z)
b = (x + y + z) - a - c
print("Los numeros son: {} , {} , {}". format(a,b,c))