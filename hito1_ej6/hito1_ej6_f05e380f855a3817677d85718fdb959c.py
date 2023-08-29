#Ordenar tres números
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))
num3 = int(input("Ingrese un tercer número: "))
menor = min(num1, num2, num3)
mayor = max(num1, num2, num3)
inter = (num1 + num2 + num3) - menor - mayor
print("los números ordenados de menor a mayor son: ", menor, ",", inter, ",",mayor)