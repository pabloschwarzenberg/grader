#Ordenar tres números
marcas = []
while len(marcas)!= 3:
    x = int(input("Ingrese un valor: "))
    marcas.append(x)
    marcas.sort()
print(marcas)     