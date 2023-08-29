#Conversión de Decimal a Binario
name = input("Ingresa tu nombre: ")
print("Hola estudiante", name)
num = int(input("Ingrese número decimal: "))

lista = []

while num>0:

  restante = int(num%2)

  lista.append(restante)

  num = (num-restante)/2

num_bin = ""

for e in lista[::-1]:

  num_bin = num_bin + str(e)

print("El resultado del numero que ingresaste es:"+str(num_bin))
