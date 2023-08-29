#Ordenar tres números
num = []

opcion = 1
contador = 0

while opcion != 0 and contador < 3:
    opcion = int(input("Ingrese número: "))
    num.append(opcion)
    contador += 1
    
num.sort()

print(num)    