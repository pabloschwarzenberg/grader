import random

# Lista de palabras secretas
palabras_secretas = ["perro", "gato", "elefante", "leon", "jirafa"]

# Función para ocultar letras aleatoriamente en la palabra secreta
def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = ""
    for i in range(len(palabra)):
        if i in letras_ocultas:
            nueva_palabra += "_"
        else:
            nueva_palabra += palabra[i]
    return nueva_palabra

# Función para revisar si una letra existe en la palabra secreta
def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra
if __name__ == "__main__":
  
  # Escoger aleatoriamente la palabra secreta y la cantidad de letras a mostrar
  palabra_secreta = random.choice(palabras_secretas)
  cantidad_letras = random.randint(1, len(palabra_secreta)-1)
  
  # Ocultar las letras en la palabra secreta
  palabra_mostrada = ocultar_letras(palabra_secreta, cantidad_letras)
  
  # Comenzar el juego
  intentos = 7
  while intentos > 0:
      print("Adivina la palabra:", palabra_mostrada)
      letra = input("Ingresa una letra o arriesga la palabra completa: ")
      if letra == palabra_secreta:
          print("¡Ganaste!")
          break
      elif letra in palabra_secreta:
          palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
          if "_" not in palabra_mostrada:
              print("¡Ganaste!")
              break
          else:
              print("¡Correcto!")
      else:
          intentos -= 1
          print("¡Incorrecto! Te quedan", intentos, "intentos.")
          
  if intentos == 0:
      print("¡Perdiste! La palabra era", palabra_secreta)
  