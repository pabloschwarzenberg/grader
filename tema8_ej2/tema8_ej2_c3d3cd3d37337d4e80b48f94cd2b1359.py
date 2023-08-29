def buscarTodas(a, b):
  posiciones = ""
  coordenadas = 0
  for i in a:
    if i==b:
      if posiciones=="":
        strcoordenadas = str(coordenadas)
        posiciones += strcoordenadas
        coordenadas += 1
      else:
        posiciones += " "
        strcoordenadas = str(coordenadas)
        posiciones += strcoordenadas
        coordenadas += 1
    else:
      coordenadas += 1
  return posiciones    
  