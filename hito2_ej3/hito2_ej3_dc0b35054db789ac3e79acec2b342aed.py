# Leer el string con la secuencia y el entero n
s = input("Ingrese un string: ")
n = int(input("Ingrese un entero n: "))

# Inicializar un diccionario vacío para almacenar los substrings y sus frecuencias
substrings = {}

# Generar todos los substrings de largo n y actualizar el diccionario
for i in range(len(s) - n + 1):
  # Obtener el substring usando rebanado de strings
  sub = s[i:i+n]
  # Si el substring ya está en el diccionario, incrementar su frecuencia en 1
  if sub in substrings:
    substrings[sub] += 1
  # Si no, agregarlo al diccionario con frecuencia 1
  else:
    substrings[sub] = 1

# Inicializar una variable booleana para indicar si hay o no substrings únicos
hay_unicos = False

# Recorrer el diccionario y imprimir solo los substrings que tengan frecuencia 1
for sub, freq in substrings.items():
  if freq == 1:
    # Imprimir el substring
    print(sub)
    # Cambiar el valor de la variable booleana a verdadero
    hay_unicos = True

# Si no hay substrings únicos, imprimir el mensaje "ninguna"
if not hay_unicos:
  print("ninguna")
      