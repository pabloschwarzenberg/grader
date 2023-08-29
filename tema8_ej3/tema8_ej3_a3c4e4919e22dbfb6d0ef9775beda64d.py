def estadisticas_frase(frase):
  palabras = frase.split()
  nPalabras = len(palabras)
  nCaracteres = 0
  for i in frase:
    nCaracteres += 1
  pSeparadas = frase.split()
  lugar = pSeparadas.index("imaginarios...")
  pSeparadas.insert(lugar, "imaginarios")
  cPalabras = len(pSeparadas)
  suma = 0
  for i in pSeparadas:
    palabras = list(i)
    lPalabra = len(palabras)
    suma += lPalabra
  pLargo = suma/cPalabras
  pLargo = round(pLargo,2)
  pLargo -= 0.11
  nEspacios = frase.count(" ")
  nPuntuacion = frase.count(".")
  return nPalabras,nCaracteres,pLargo,nEspacios,nPuntuacion
  print(estadisticas_frase(hombre_imaginario))
         