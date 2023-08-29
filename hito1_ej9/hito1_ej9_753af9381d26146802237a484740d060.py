#Sistema de Ecuaciones
primerT  = float(input("Numero 1:"))
segundoT = float(input("Numero 2:"))
tercerT  = float(input("Numero 3:"))
cuartoT  = float(input("Numero 4:"))   
quintoT  = float(input("Numero 5:"))
sextoT   = float(input("Numero 6:"))

#ordenar al ecuacion
x = (tercerT * quintoT - segundoT * sextoT) // (primerT * quintoT - segundoT * cuartoT)
y = (primerT * sextoT - tercerT * cuartoT) // (primerT * quintoT - segundoT * cuartoT)

#imprimir variables solicitadas
print("x=" +str(x) + "y="+str(y))      