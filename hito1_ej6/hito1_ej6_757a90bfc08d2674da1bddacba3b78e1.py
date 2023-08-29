#ordenar tres numeros
a = int(input("ingresa tu primer numero: "))
b = int(input("ingresa tu segundo numero: "))
c = int(input("ingresa tu tercer numero: "))

maximo = max(a, b, c)
minimo = min(a, b, c)
j = (a + b + c) - maximo - minimo
print("De menor a mayor sus numeros son: ", minimo,",",j,",",maximo)