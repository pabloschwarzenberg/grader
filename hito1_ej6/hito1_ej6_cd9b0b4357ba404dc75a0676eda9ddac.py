X = eval(input("Ingrese su primer dígito: "))
Y = eval(input("Ingrese su segundo dígito: "))
Z = eval(input("Ingrese su tercer dígito: "))

Ma = max(X,Y,Z)
print("el número mayor es: ", Ma)

Mi = min(X,Y,Z)
print("el número menor es: ", Mi)

D = (X + Y + Z) - Ma - Mi
print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma)