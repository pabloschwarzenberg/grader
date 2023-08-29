# Importar el módulo random para generar números aleatorios
import random

# Definir una función que oculta algunas letras de una palabra
def ocultar_letras(palabra, cantidad):
  # Convertir la palabra en una lista de caracteres
  lista = list(palabra)
  # Definir una variable para controlar el número de letras ocultadas
  ocultadas = 0
  # Mientras el número de letras ocultadas sea menor que la cantidad
  while ocultadas < cantidad:
    # Generar un índice aleatorio entre 0 y la longitud de la palabra menos 1
    indice = random.randint(0, len(palabra) - 1)
    # Si la letra en ese índice no está oculta
    if lista[indice] != "_":
      # Reemplazar la letra por un guión bajo
      lista[indice] = "_"
      # Incrementar el número de letras ocultadas
      ocultadas += 1
  # Convertir la lista de caracteres en una cadena y retornarla
  return "".join(lista)

# Definir una función que revisa si una letra está en la palabra secreta y la muestra
def revisar_letra(palabra_secreta, palabra, letra):
  # Convertir la palabra secreta y la palabra con letras ocultas en listas de caracteres
  lista_secreta = list(palabra_secreta)
  lista = list(palabra)
  # Recorrer los índices de las listas
  for i in range(len(lista)):
    # Si la letra en el índice i de la lista secreta es igual a la letra ingresada
    if lista_secreta[i] == letra:
      # Reemplazar el guión bajo por la letra en el índice i de la lista con letras ocultas
      lista[i] = letra
  # Convertir la lista con letras ocultas en una cadena y retornarla
  return "".join(lista)

# Si el programa se ejecuta como principal
if __name__ == "__main__":
  # Crear una lista con palabras secretas
  palabras = ["lepidoptero", "ornitorrinco", "hipopotamo", "escafandra", "paralelepipedo"]
  # Escoger una palabra secreta al azar y guardarla en una variable
  palabra_secreta = random.choice(palabras)
  # Escoger un número aleatorio de letras a ocultar entre 1 y la mitad de la longitud de la palabra secreta
  cantidad = random.randint(1, len(palabra_secreta) // 2)
  # Llamar a la función ocultar_letras con la palabra secreta y la cantidad y guardar el resultado en una variable
  palabra = ocultar_letras(palabra_secreta, cantidad)
  # Imprimir la palabra con algunas letras ocultas
  print("La palabra es:", palabra)
  # Definir una variable para controlar el número de intentos
  intentos = 0
  # Definir una variable para indicar si el jugador adivinó o no
  adivino = False

  # Mientras el número de intentos sea menor que 7 y el jugador no haya adivinado
  while intentos < 7 and not adivino:
    # Pedir al jugador que ingrese una letra o arriesgarse a decir la palabra completa
    entrada = input("Ingresa una letra o arriesga la palabra completa: ")
    # Si la entrada es igual a la palabra secreta
    if entrada == palabra_secreta:
      # Imprimir un mensaje de felicitación y la palabra secreta
      print("Adivinaste, la palabra era", palabra_secreta)
      # Cambiar la variable adivino a True para salir del ciclo
      adivino = True
    # Si la entrada es una sola letra
    elif len(entrada) == 1:
      # Llamar a la función revisar_letra con la palabra secreta, la palabra con letras ocultas y la entrada y guardar el resultado en una variable
      nueva_palabra = revisar_letra(palabra_secreta, palabra, entrada)
      # Si la nueva palabra es igual a la anterior, significa que la letra no estaba en la palabra secreta
      if nueva_palabra == palabra:
        # Imprimir un mensaje de error
        print("La letra", entrada, "no está en la palabra")
      else:
        # Actualizar la palabra con letras ocultas con la nueva palabra
        palabra = nueva_palabra
        # Imprimir la nueva palabra
        print("La palabra es:", palabra)
        # Si la nueva palabra es igual a la palabra secreta, significa que el jugador adivinó todas las letras
        if nueva_palabra == palabra_secreta:
          # Imprimir un mensaje de felicitación y la palabra secreta
          print("Adivinaste, la palabra era", palabra_secreta)
          # Cambiar la variable adivino a True para salir del ciclo
          adivino = True
    else:
      # Imprimir un mensaje de error indicando que la entrada no es válida
      print("Entrada no válida")
    # Incrementar el número de intentos
    intentos += 1

  # Si el jugador no adivinó después de los 7 intentos
  if not adivino:
    # Imprimir un mensaje de fracaso y la palabra secreta
    print("No adivinaste, la palabra era", palabra_secreta)
