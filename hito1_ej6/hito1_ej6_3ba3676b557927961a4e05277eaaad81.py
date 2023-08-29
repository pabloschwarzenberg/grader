#Ordenar tres números
a = int(input("Ingres valor de A: "))
b = int(input("Ingres valor de B: "))
c = int(input("Ingres valor de C: "))

a1 = min(a, b, c)
c1 = max(a, b, c)
b1 = (a + b + c) - a1 - c1

print("los numeros ordenados son: {}, {}, {}".format(a1, b1, c1))