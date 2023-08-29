#Sistema de Ecuaciones
def solucion_sistema_ecuaciones(a, b, c, d, e, f):
    determinate = a*e - b*d

    if  determinate !=0:
        x = (c*e - b*f) / determinate
        y = (a*f - c*d) / determinate

         return x, y
    else:
         return None, None

print("Digitos los valores para a, b, c, d, e, y f: ")
a, b, c, d, e, f, =map(float, input().split())