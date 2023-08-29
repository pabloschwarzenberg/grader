#Ordenar tres números
A = int (input ('Ingrese su primer número: '))
B = int (input ('Ingrese su segundo número: '))
C = int (input ('Ingrese su tercer número: '))

mayor = max (A,B,C)
print ("El número mayor es: ", mayor)
menor = min (A,B,C)
print ("El número menor es: ", menor)

RES = (A + B + C) - mayor - menor

print ("De menor a mayor el orden es ", menor, ",", RES, ",", mayor)
   