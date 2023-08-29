# Importar el módulo
import Levenshtein

# Definir la función levenshtein
def levenshtein(palabra1, palabra2):
  # Calcular la distancia de Levenshtein entre las dos palabras
  distancia = Levenshtein.distance(palabra1, palabra2)

  # Retornar el string correspondiente según el valor de la distancia
  if distancia > 1:
    return "+1"
  elif distancia == 1:
    # Comprobar si hay que insertar o borrar una letra
    if len(palabra1) != len(palabra2):
      return "IB"
    # Comprobar si hay que sustituir una letra
    else:
      return "1S"
  elif distancia == 0:
    return "0D"

