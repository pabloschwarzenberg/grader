#Ordenar tres números

X = int(input("ingrese el primer numero:"))
Y = int(input("Ingrese el segundo numero:"))
Z = int(input("ingrese el tercer numero"))
Max= max(X,Y,Z)
Min= min(X,Y,Z)
D = (X + Y + Z) - Max - Min
print(Min,",", D ,", ",Max)    