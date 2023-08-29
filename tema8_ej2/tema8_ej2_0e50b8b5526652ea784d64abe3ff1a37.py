def buscarTodas(a,b):
  a = a.lower()
  posiciones = ''
  for posicion, letra in enumerate(a):
    if b==letra:
      posiciones += str(posicion) + ' '
  return (posiciones.rstrip(' '))