#Ordenar tres números
a = int(input ( "ingrese un número: ") )
b = int(input ( "ingrese un número: ") )
c = int(input ( "ingrese un número: ") )

d = min(a , b , c)
e = max(a , b , c)
g = (a + b + c) - d - e  

print("El orden de menor a mayor es: {}, {}, {}".format(d, g, e))