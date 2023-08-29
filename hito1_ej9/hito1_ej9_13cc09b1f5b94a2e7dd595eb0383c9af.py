#Sistema de Ecuaciones
Primer_termino  = float(input("Numero 1:"))
Segundo_termino = float(input("Numero 2:"))
Tercer_termino  = float(input("Numero 3:"))
Cuarto_termino  = float(input("Numero 4:"))   
Quinto_termino  = float(input("Numero 5:"))
Sexto_termino   = float(input("Numero 6:"))

#ordenar al ecuacion

X = (Tercer_termino * Quinto_termino - Segundo_termino * Sexto_termino) // (Primer_termino * Quinto_termino - Segundo_termino * Cuarto_termino)
Y = (Primer_termino * Sexto_termino - Tercer_termino * Cuarto_termino) // (Primer_termino * Quinto_termino - Segundo_termino * Cuarto_termino)

#imprimir variables solicitadas

print("X=" +str(X) + "Y="+str(Y))      