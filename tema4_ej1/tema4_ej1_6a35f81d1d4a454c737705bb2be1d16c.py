import random # Importamos el módulo random para usar funciones de aleatoriedad

# Definimos una lista con palabras secretas
palabras = ["lepidoptero", "ornitorrinco", "hipopotamo", "espeleologia", "criptozoologia"]

# Definimos una función que oculta algunas letras de una palabra
def ocultar_letras(palabra, cantidad):
  # Esta función recibe una palabra y una cantidad de letras a ocultar, y retorna la palabra con esas letras reemplazadas por "_"
  # Creamos una lista vacía para guardar las posiciones de las letras a ocultar
  posiciones = []
  # Mientras la lista tenga menos elementos que la cantidad indicada
  while len(posiciones) < cantidad:
    # Generamos un número aleatorio entre 0 y la longitud de la palabra menos 1
    posicion = random.randint(0, len(palabra) - 1)
    # Si el número no está en la lista
    if posicion not in posiciones:
      # Lo agregamos a la lista
      posiciones.append(posicion)
  # Creamos una lista vacía para guardar la palabra modificada
  nueva_palabra = []
  # Recorremos la palabra original por índice y letra
  for i, letra in enumerate(palabra):
    # Si el índice está en la lista de posiciones
    if i in posiciones:
      # Agregamos un "_" a la nueva palabra
      nueva_palabra.append("_")
    else:
      # Si no, agregamos la letra original a la nueva palabra
      nueva_palabra.append(letra)
  # Retornamos la nueva palabra como una cadena, uniendo los elementos de la lista con "".join()
  return "".join(nueva_palabra)

# Definimos una función que revisa si una letra está en la palabra secreta y la muestra en la palabra oculta
def revisar_letra(palabra_secreta, palabra, letra):
  # Esta función recibe la palabra secreta, la palabra con letras ocultas y una letra a revisar, y retorna la palabra con las letras actualizadas
  # Creamos una lista vacía para guardar la palabra actualizada
  nueva_palabra = []
  # Recorremos la palabra secreta y la palabra oculta al mismo tiempo con zip()
  for letra_secreta, letra_oculta in zip(palabra_secreta, palabra):
    # Si la letra secreta es igual a la letra a revisar
    if letra_secreta == letra:
      # Agregamos la letra a la nueva palabra
      nueva_palabra.append(letra)
    else:
      # Si no, agregamos la letra oculta a la nueva palabra
      nueva_palabra.append(letra_oculta)
  # Retornamos la nueva palabra como una cadena, uniendo los elementos de la lista con "".join()
  return "".join(nueva_palabra)

# Probamos el juego con algunos ejemplos
if __name__ == "__main__":
  # Escogemos una palabra secreta al azar de la lista de palabras
  palabra_secreta = random.choice(palabras)
  # Escogemos una cantidad de letras a ocultar al azar entre 1 y la mitad de la longitud de la palabra secreta
  cantidad = random.randint(1, len(palabra_secreta) // 2)
  # Ocultamos algunas letras de la palabra secreta usando la función ocultar_letras()
  palabra = ocultar_letras(palabra_secreta, cantidad)
  # Imprimimos la palabra con letras ocultas
  print("La palabra secreta es:", palabra)
  # Inicializamos una variable para contar los intentos del jugador
  intentos = 0
  # Inicializamos una variable para controlar el ciclo del juego
  seguir = True
  # Iniciamos el ciclo del juego
  while seguir:
    # Solicitamos al jugador que ingrese una letra o arriesgue la palabra completa
    entrada = input("Ingrese una letra o arriesgue la palabra completa: ")
    # Si la entrada es igual a la palabra secreta
    if entrada == palabra_secreta:
      # Imprimimos un mensaje de felicitación
      print("¡Felicitaciones! Has adivinado la palabra secreta.")
      # Cambiamos el valor de seguir para terminar el ciclo
      seguir = False
    # Si la entrada es una sola letra
    elif len(entrada) == 1:
      # Aumentamos el contador de intentos en 1
      intentos += 1
      # Revisamos si la letra está en la palabra secreta y actualizamos la palabra con letras ocultas
      palabra = revisar_letra(palabra_secreta, palabra, entrada)
      # Imprimimos la palabra actualizada
      print("La palabra secreta es:", palabra)
      # Si la palabra ya no tiene letras ocultas
      if "_" not in palabra:
        # Imprimimos un mensaje de felicitación
        print("¡Felicitaciones! Has adivinado la palabra secreta.")
        # Cambiamos el valor de seguir para terminar el ciclo
        seguir = False
    # Si la entrada no es válida
    else:
      # Imprimimos un mensaje de error
      print("Entrada inválida. Debe ingresar una letra o arriesgar la palabra completa.")
    # Si el jugador ha usado los 7 intentos
    if intentos == 7:
      # Imprimimos un mensaje de derrota
      print("Lo siento, has perdido. La palabra secreta era:", palabra_secreta)
      # Cambiamos el valor de seguir para terminar el ciclo
      seguir = False
       