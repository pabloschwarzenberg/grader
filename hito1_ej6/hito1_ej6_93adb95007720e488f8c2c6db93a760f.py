#Ordenar tres números
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
lista = [a, b, c]
menamas = sorted(lista)
print("a, b y c ordenados de menor a mayor son: " + str(menamas))