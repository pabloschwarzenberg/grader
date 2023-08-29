#Intruccion
X = eval(input("Escriba primer numero: "))
Y = eval(input("Segundo numero: "))
Z = eval(input("Tercer numero: "))
#Parametros
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
D = (X + Y + Z) - Ma - Mi
#Prints
print("el número mayor es: ", Ma)
print("el número menor es: ", Mi)
print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma) 