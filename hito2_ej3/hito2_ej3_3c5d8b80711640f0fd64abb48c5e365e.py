# Definir una función que recibe un string y un entero n, y retorna una lista de los substrings de largo n que aparecen una única vez
def substrings_unicos(s, n):
  # Definir una lista vacía para guardar los substrings
  substrings = []

  # Definir un diccionario vacío para contar las ocurrencias de cada substring
  ocurrencias = {}

  # Recorrer el string desde la posición 0 hasta la posición len(s) - n
  for i in range(len(s) - n + 1):
    # Obtener el substring de largo n que empieza en la posición i
    substring = s[i:i+n]

    # Verificar si el substring está en el diccionario o no
    if substring in ocurrencias:
      # Incrementar el valor asociado al substring en uno
      ocurrencias[substring] += 1
    else:
      # Agregar el substring al diccionario con el valor inicial de uno
      ocurrencias[substring] = 1
  
  # Recorrer los items del diccionario
  for substring, valor in ocurrencias.items():
    # Verificar si el valor es igual a uno o no
    if valor == 1:
      # Agregar el substring a la lista de substrings
      substrings.append(substring)
  
  # Retornar la lista de substrings
  return substrings

# Pedir al usuario que ingrese un string y un entero n
s = input("Ingrese un string: ")
n = int(input("Ingrese un entero n: "))

# Llamar a la función con los valores ingresados y guardar el resultado en una variable
resultado = substrings_unicos(s, n)

# Verificar si la lista de resultado está vacía o no
if len(resultado) == 0:
  # Imprimir el mensaje "ninguna"
  print("ninguna")
else:
  # Recorrer la lista de resultado e imprimir cada elemento en una línea
  for substring in resultado:
    print(substring)
