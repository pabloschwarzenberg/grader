#Ordenar tres números
X = int(input("Ingrese un numero: "))
Y = int(input("Ingrese un segundo numero: "))
Z = int(input("Ingrese un tercer numero: "))

Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
medio= (X + Y + Z)- Mi -Ma
print("los numeros de menor a mayor son: {},{},{}".format(Mi,medio,Ma))