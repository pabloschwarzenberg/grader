#Ordenar tres números
x = int(input("Primer numero entero:" ))
y = int(input("Segundo numero entero:" ))
z = int(input("Tercer numero entero:" ))
ma = max (x , y , z)
mi = min (x , y, z)
me = (x + y + z) - ma - mi
print("Los numeros de menor a mayor son: ", mi, ",", me, ",", ma)