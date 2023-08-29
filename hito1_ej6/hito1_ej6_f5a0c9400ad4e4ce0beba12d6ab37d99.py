#Ordenar tres números
X = int(input("Ingrese un primer número: "))
Y = int(input("Ingrese un segundo número: "))
Z = int(input("Ingrese un tercer número: "))

mi = min(X, Z, Y)
ma = max(X, Z, Y)
inter = (X + Z + Y) - mi - ma
print("numeros ordenados: ", mi,", ", inter,", ", ma,".")