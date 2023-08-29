#Ordenar tres números

NumUno = int(input('Escriba el primer numero :'))
NumDos = int(input('Escriba el segundo numero :'))
NumTres = int(input('Escriba el tercer numero :'))
#DESARROLLO
a = min( NumUno , NumDos , NumTres )
c = max( NumUno , NumDos , NumTres )
b = ( NumUno + NumDos + NumTres ) - a - c

#Salida
print('Los numeros ordenados de menor a mayor : {} , {} , {}' .format (a,b,c))      