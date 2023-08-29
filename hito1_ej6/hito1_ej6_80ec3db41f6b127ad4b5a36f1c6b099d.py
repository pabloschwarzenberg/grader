#Ordenar tres números

X = eval(input("Ingrese un número: "))
Y = eval(input("Ingrese un segundo número: "))
Z = eval(input("Ingrese un tercer número: "))
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
D = (X + Y + Z) - Ma -Mi
print("De menor a mayor el órden es: ", Mi ,",", D , ",", Ma)