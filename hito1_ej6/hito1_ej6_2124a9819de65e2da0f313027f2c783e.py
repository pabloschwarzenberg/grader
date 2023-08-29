#Ordenar tres números
numero1 = int(input("escriba el primer numero: "))
numero2 = int(input("escriba el segundo numero: "))
numero3 = int(input("escriba el tercer numero: "))

x = min(numero1, numero2, numero3)
y = max(numero1, numero2, numero3)
z = (numero1+numero2+numero3)-x-y

print("los numeros ordenados son", (x,z,y))