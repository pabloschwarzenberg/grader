#Sistema de Ecuaciones
#ax + by = c
#dx + ey = f
def solucion_sistema_ecucacion(a, b, c, d , e, f):
  determinante = a*e - b*d
  if determinante != 0:
    x = (c*e - b*f) / determinante
    y = (a*f - c*d) / determinante

    return x, y
  else: 
    return None, None

print('Digite los valores de a, b, c, d, e, f: ')
a, b, c, d, e, f =input(float)

print(solucion_sistema_ecucacion(a, b, c, d, e, f))
