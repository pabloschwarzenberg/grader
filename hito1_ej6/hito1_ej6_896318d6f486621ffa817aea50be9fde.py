#Ordenar tres números
N1 = eval(input("Ingrese su primer número: "))
N2 = eval(input("Ingrese su segundo número: "))
N3 = eval(input("Ingrese su tercer número: "))

Ma = max (N1,N2,N3)
Mi = min (N1,N2,N3)

M = (N1 + N2 + N3) - Ma - Mi

print ("El orden de sus numeros es ",Mi,",",M,",", Ma)