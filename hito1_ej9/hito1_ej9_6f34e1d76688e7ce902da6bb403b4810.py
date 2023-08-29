#Sistema de Ecuaciones
def solucionSistemaEcuaciones(a, b, c, d, e, f):
  determinante = a*e - b*d
  if determinante != 0:
    x = (c*e - b*f) / determinante
    y = (c*f - c*d) / determinante
    return x, y
  else:
    return None, None
print("Digite los valores para a, b, c, d, e y f: ")
a, b, c, d, e, f = map(float, input().split())
print(solucionSistemaEcuaciones(a, b, c, d, e, f))