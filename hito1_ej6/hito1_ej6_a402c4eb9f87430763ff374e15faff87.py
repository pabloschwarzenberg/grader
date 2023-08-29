#Ordenar tres números
print ("Ingrese 3 números")
x = eval(input("Ingrese el primer numero\n"))
y = eval(input("Ingrese el segundo numero\n"))
z = eval(input("Ingrese el tercer numero\n"))
numeros = (x, y, z)
ordenados = sorted(numeros)
print ("De menor a mayor el orden es ", ordenados)