#Ingreso de los valores
Z = eval(input("Ingrese un valor: "))

X = eval(input("Ingrese un segundo valor: "))

Y = eval(input("Ingrese un tercer valor: "))

#Valores de menor a mayor

menor= min(Z,X,Y)


mayor= max(Z,X,Y)

#Operacion procesamiento

operacion = (Z + X + Y) - mayor - menor

#Salida



print("El orden correspondiente es: ", menor ," , ", operacion , " , ", mayor) 
