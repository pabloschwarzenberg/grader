# Definir una función que encuentre los substrings de largo n que aparezcan una única vez en un string
def encontrar_substrings_unicos(string, n):
  # Crear un diccionario vacío para almacenar los substrings y sus frecuencias
  frecuencias = {}
  # Recorrer el string desde el inicio hasta el final menos n
  for i in range(len(string) - n + 1):
    # Obtener el substring de largo n que empieza en la posición i
    substring = string[i:i+n]
    # Si el substring ya está en el diccionario, incrementar su frecuencia en uno
    if substring in frecuencias:
      frecuencias[substring] += 1
    # Si no, agregarlo al diccionario con frecuencia uno
    else:
      frecuencias[substring] = 1
  # Crear una lista vacía para almacenar los substrings únicos
  unicos = []
  # Recorrer el diccionario de frecuencias
  for substring, frecuencia in frecuencias.items():
    # Si la frecuencia es uno, agregar el substring a la lista de únicos
    if frecuencia == 1:
      unicos.append(substring)
  # Retornar la lista de substrings únicos
  return unicos

# Pedir al usuario que ingrese un string y un entero n
string = input("Ingrese un string: ")
n = int(input("Ingrese un entero n: "))

# Llamar a la función encontrar_substrings_unicos con el string y el n ingresados
substrings_unicos = encontrar_substrings_unicos(string, n)

# Imprimir el resultado según la longitud de la lista de substrings únicos
if len(substrings_unicos) == 0:
  print("Ninguna")
else:
  for substring in substrings_unicos:
    print(substring)
