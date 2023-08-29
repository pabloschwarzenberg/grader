def estaditicas_frase (frase):
  caracteres = len(frase) 
  num_espacios = 0 
  num_puntuacion = 0
  j = " "
  for j in frase: 
    if j == " ":
      num_espacios = num_espacios + 1
    if j == ".":
      num_puntuacion = num_puntuacion + 1 
  frase = frase.strio(".")
  palabras= len(frase.split())

  1_prom=list(frase.split())
  sumatoria = 0 
  suma = 0 
  for i in range(palabras): 
    sumatoria = len (1_prom[i])
    i = i + 1 
    suma = suma + sumatoria 
    promedio = suma/palabras
    return palabras, caracteres, promedio, num_espacios, num_puntuacion

         