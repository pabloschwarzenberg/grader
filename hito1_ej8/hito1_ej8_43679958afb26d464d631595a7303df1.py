#Descomponer un número
n = int(input("Ingrese un numero de 4 digitos: "))
M = (n//1000)
C = ((n//100)%10)
D = ((n//10)%10)
U = ((n//1)%10)
print("La descomposicion queda como", M,"M+", C,"C+", D,"D+", U,"U+")   