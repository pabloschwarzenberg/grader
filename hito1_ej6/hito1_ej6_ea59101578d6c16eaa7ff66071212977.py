#Ordenar tres números
A = 0
B = 0
C = 0
print("ingrese 3 numeros :") 

A = int(input ("ingresa el primer numero: "))
B = int(input ("ingresa el segundo numero: "))
C = int(input ("ingresa el tercer numero: "))

mayor = max(A,B,C)
menor = min(A,B,C)
medio = (A+B+C)- mayor - menor

print("los numeros ordenados ascendentemente son : {},{},{}" .format(menor, medio, mayor))
