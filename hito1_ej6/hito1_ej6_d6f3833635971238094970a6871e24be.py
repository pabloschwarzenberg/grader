#Ordenar tres números
valor1 = int(input("Ingrese un primer número")) 
valor2 = int(input("Ingrese un segundo número")) 
valor3 = int(input("Ingrese un tercer número"))
x = min(valor1, valor2, valor3)
z = max(valor1, valor3 , valor2)
y = (valor1 + valor2 + valor3) - z - x
print("Los números ordenados de menor a mayor: {} , {} , {}".format(x, y, z))