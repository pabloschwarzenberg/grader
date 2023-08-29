#Ordenar tres números
v1 = int(input("ingrese un 1er numero: \n"))
v2 = int(input("ingrese un 2er numero: \n"))
v3 = int(input("ingrese un 3er numero: \n"))
a = min(v1,v2,v3)
c = max(v1,v2,v3)
b = (v1+v2+v3) - a - c
print("Ordenados de menor a mayor quedarían: {}, {}, {},".format(a,b,c))