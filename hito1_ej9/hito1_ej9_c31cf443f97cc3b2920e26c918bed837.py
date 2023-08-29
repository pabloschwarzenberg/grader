#Sistema de Ecuaciones
def solucion_sistema_ecuaciones(A, B, C, D, E, F):
    determinante = A*E - B*D
    if determinante !=0:
        x=(C*E - B*F) / determinante
        y = (A*F -C*D) /determinante
        
        return x, y
    else:
        return None, None
        
print ("Ingrese los valores para A,B,C,D,E,F:")
  A, B, C, D, E, F = map(float, input().split())

print (solucion_sistema_ecuaciones(A, B, C, D, E, F))   