import random

def ocultar_letras(palabra, cantidad):
  letras_ocultas = random.sample(range(len(palabra)), cantidad)
  palabra_oculta = list(palabra)
  for indice in letras_ocultas:
    palabra_oculta[indice] = "_"
  return"".join(palabra_oculta)
  
def revisar_letra(palabra_secreta, palabra_mostrada, letra):
  nueva_palabra = list(palabra_mostrada)
  for i in range(len(palabra_secreta)):
    if palabra_secreta[i] == letra:
      nueva_palabra[i] = letra
  return "".join(nueva_palabra)
  
if __name__=="__main__":
  palabras_secretas = ["python", "programacion", "computador", "juego", "cadena"]
  palabra_secreta = random.choice(palabras_secretas)
  letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
  palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
  intentos = 7
  
  print("Bienvenido a adivina la palabra")
  print("la palabra secreta tiene", len(palabra_secreta), "letras")
  print("tienes 7 intentos")
  
  while intentos > 0:
    print("\nPalabra actual:", palabra_mostrada)
    print("intentos restantes:", intentos)
    opcion = input("ingresa una letra o la palabra completa:")
    
    if len(opcion) == 1:
      palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
      if opcion not in palabra_secreta:
        intentos -= 1
    else:
      intentos -= 1
  
  if intentos == 0:
    print("\nHas perdido, la palabra secreta era:", palabra_secreta)