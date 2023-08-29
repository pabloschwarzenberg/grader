def estadisticas_frase (s):
  # Inicializar las variables que almacenarán los resultados
  num_palabras = 0
  num_caracteres = 0
  largo_promedio = 0
  num_espacios = 0
  num_puntuacion = 0

  # Dividir el string en una lista de palabras
  lista_palabras = s.split ()

  # Contar el número de palabras
  num_palabras = len (lista_palabras)

  # Iterar sobre cada palabra de la lista
  for palabra in lista_palabras:
    # Contar el número de caracteres que no son especiales
    for caracter in palabra:
      if caracter.isalpha ():
        num_caracteres += 1

    # Contar el número de espacios y caracteres de puntuación después de cada palabra
    if palabra[-1].isspace ():
      num_espacios += 1
    elif not palabra[-1].isalpha ():
      num_puntuacion += 1

  # Calcular el largo promedio de las palabras
  largo_promedio = num_caracteres / num_palabras

  # Retornar los resultados como una tupla
  return (num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion)
