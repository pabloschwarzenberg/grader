#Suma de los N primeros números
print("La suma de los primeros n numeros naturales dada por n(n + 1)/2.")
A=int(input("INGRESE n: "))
if A<=0:
    print("ERROR")
    print("INGRESE UN NUMERO NATURAL (SOLO POSITIVOS)")
else:
    O=(A*(A+1))/2
    print("LA SUMA DE LOS PRIMEROS", A, "NUMEROS NATURALES ES IGUAL A: ", O)      