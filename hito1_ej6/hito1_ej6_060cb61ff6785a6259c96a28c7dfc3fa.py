#Ordenar tres números
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
ordenados = sorted((a, b, c))
print(','.join([str(p) for p in ordenados]))
