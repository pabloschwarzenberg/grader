#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

menor = min(num1, num2, num3)
mayor = max(num1, num2, num3)
medio = (num1 + num2 + num3) - menor - mayor

print("Los números ordenados de menor a mayor son:", menor, ",", medio, ",", mayor)
