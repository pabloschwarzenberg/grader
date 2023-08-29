#Descomponer un número
num=int(input("Ingrese numero"))
n = str(num)
print('''Numero descompuesto: {}'''.format(num))
print("Milesima: {}".format(n[0]))
print("Unidad: {}".format(n[3]))
print("Decena: {}".format(n[2]))
print("Centena: {}".format(n[1]))      