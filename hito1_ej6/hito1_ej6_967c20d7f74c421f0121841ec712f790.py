#Ordenar tres números
x = int(input("ingrese numero 1: " ))
y = int(input("ingrese numero 2: " ))
z = int(input("ingrese numero 3: " ))
#funcion min  muestra como resultado el minimo de las tres varibles xyz
a = min(x,y,z)
#funcion max  muestra como resultado  el maximo de las tres variables xyz
c = max(x,y,z)
b = (x+y+z)-a-c
print('numeros de menor a mayor:{},{},{}'.format(a,b,c))    