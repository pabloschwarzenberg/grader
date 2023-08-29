def buscarTodas(a,b):
  posiciones = ""
  posicion = 0
  while posicion != -1:
    posicion = a.find(b,posicion)
    if posicion != -1:
      posiciones = posiciones + " " + str(posicion)
      posicion += 1
  return posiciones.lstrip()