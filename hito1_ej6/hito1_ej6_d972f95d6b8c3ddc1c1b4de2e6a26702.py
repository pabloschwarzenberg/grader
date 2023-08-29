#Ordenar tres números

a = eval(input("Ingrese el primer número: "))
b = eval(input("Ingrese el segundo número: "))
c = eval(input("Ingrese el tercer número: "))

ma = max(a,b,c)
mi = min(a,b,c)

T = (a + b +c) - ma - mi

print("Los números ordenados de menor a mayor son: ", mi , "," , T , "," , ma)
