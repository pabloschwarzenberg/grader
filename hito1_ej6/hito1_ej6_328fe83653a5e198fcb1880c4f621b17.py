print ("programa para ordenar 3 enteros")
n1 = int(input("ingrese n1: "))
n2 = int(input("ingrese n2: "))
n3 = int(input("ingrese n3: "))

minimo = min(n1, n2, n3)
maximo = max (n1,n2,n3)
intermedio = (n1+n2+n3) - maximo - minimo

print ("los numeros ordenados son: {}, {}, {}" .format(minimo,intermedio,maximo))