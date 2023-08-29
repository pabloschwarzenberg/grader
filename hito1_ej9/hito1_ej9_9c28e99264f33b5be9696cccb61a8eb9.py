#Sistema de Ecuaciones
def sistema_ecuaciones(a, b, c, d, e, f):
  determinante = ((a*e) - (b*d))
  if determinante != 0:
    x = (c*e - b*f) / determinante
    y = (a*f - c*d) / determinante
    return print('x=', x, 'y=', y)
    