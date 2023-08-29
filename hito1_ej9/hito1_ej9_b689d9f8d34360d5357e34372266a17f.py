#Sistema de Ecuaciones
primer_termino  = float(input("Numero 1:"))
segundo_termino = float(input("Numero 2:"))
tercer_termino  = float(input("Numero 3:"))
cuarto_termino  = float(input("Numero 4:"))   
quinto_termino  = float(input("Numero 5:"))
sexto_termino   = float(input("Numero 6:"))

#ordenar al ecuacion

x = (tercer_termino * quinto_termino - segundo_termino * sexto_termino) // (primer_termino * quinto_termino - segundo_termino * cuarto_termino)
y = (primer_termino * sexto_termino - tercer_termino * cuarto_termino) // (primer_termino * quinto_termino - segundo_termino * cuarto_termino)

#imprimir variables solicitadas

print("x=" +str(x) + "y="+str(y))    