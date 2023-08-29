#Ordenar tres números
print("numero enteros de menor a mayor")
valor_uno= int(input("ingrese un numero entero: "))
valor_dos= int(input("ingrese un numero entero: "))
valor_tres= int(input("ingrese un numero entero: "))

a= min(valor_uno, valor_dos, valor_tres)
b= max(valor_uno, valor_dos, valor_tres)
c= (valor_uno + valor_dos + valor_tres) - a - b

print ("los numero ordenados de menor a mayor son: {},{},{}" .format(a,b,c))

