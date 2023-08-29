#Ordenar tres números
# Datos
v1 = int(input("ingrese un 1er numero: "))
v2 = int(input("ingrese un 2er numero: "))
v3 = int(input("ingrese un 3er numero: "))
# Procesamiento
a = min(v1,v2,v3)
c = max(v1,v2,v3)
b = (v1+v2+v3) - a - c
# Datos ordenados
print("Ordenados de menor a mayor quedarían: {}, {}, {},".format(a,b,c))