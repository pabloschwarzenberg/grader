#Ordenar tres números
print("Escriba 3 números y serán ordenados de menor a mayor")
numero1= int(input("Ingrese el primer numero "))
numero2= int(input("Ingrese el segundo numero "))
numero3= int(input("Ingresa el tercer numero "))

x= min(numero1, numero2, numero3)
y= max(numero1, numero2, numero3)
z= (numero1 + numero2 + numero3) - x - y

print("Los número son: ", (x, z, y))