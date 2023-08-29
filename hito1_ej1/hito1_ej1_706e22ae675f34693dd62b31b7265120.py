#Nota final
# Entrada

PT = float(input())
PI = float(input())
NE = float(input())
PP = float(input())

condicion = 1.0 < PT < 7.0 and 1.0 < PI < 7.0 and 1.0 < NE < 7.0 and 1.0 < PP < 7.0
if not condicion:
    print("Volver a pedir su nota")


# Calculo de la solucion

if condicion:
      sol = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
      print( round (sol, 1) )


# Fin
print("Fin.")   