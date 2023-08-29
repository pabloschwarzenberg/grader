#Ordenar tres números
X = eval(input("Ingrese primer numero porfavor: "))
Y = eval(input("Ingrese un segundo numero porfavor: "))
Z = eval(input("Ingrese un tercer numero porfavor: "))

Ma = max(X,Y,Z)
print("el número mayor es: ", Ma)
Mi = min(X,Y,Z)
print("el número menor es: ", Mi)

D = (X + Y + Z) - Ma - Mi

print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma)

      