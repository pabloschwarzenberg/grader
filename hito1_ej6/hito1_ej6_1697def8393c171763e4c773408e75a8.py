#Ordenar tres números
X = eval(input("Escriba un primer número: "))
Y = eval(input("Escriba un segundo número: "))
Z = eval(input("Escriba un tercer número: "))

Ma = max(X, Y, Z)
Mi = min(X, Y, Z)
##############

D = (X + Y + Z) -Ma - Mi


print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma)

      