import random

def ocultar_letras(palabra,cantidad):
  palabra = list(palabra)
  for i in range(cantidad):
      # La posición debe estár dentro de la palabra
    posicion = random.randint(0, len(palabra)-1)
      # Covertimos la palabra a una lista
    palabra[posicion] = "_"
  return "".join(palabra) 

def revisar_letra(palabra_secreta,palabra,letra):
  palabra_lista = list(palabra)
  for i in range(len(palabra_secreta)):
    if palabra_secreta[i] == letra:
      palabra_lista[i] = letra
  return "".join(palabra_lista)

         