numeros = []


for i in range(3):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)


mayor = numeros[0]
menor=numeros[0]
mediano=numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
   
    if numero <menor:
        menor=numero
    if numero > mediano:
        mediano = menor

print("menor:", menor)
print("mediano:", mediano)
print("Mayor:", mayor)