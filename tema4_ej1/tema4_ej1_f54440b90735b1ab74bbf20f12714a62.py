import random

def ocultar_letras (palabra, cantidad):
  adivinar = []
  for n in palabra:
    adivinar.append(n)
  
  contador = 0
  while contador != cantidad:
    indice = random.randint(0, len(palabra) - 1)
    if adivinar[indice] != "_":
      adivinar[indice] = "_"
      contador += 1
  
  adivinar2 = ""
  for a in adivinar:
    adivinar2 += a

  
  return adivinar2
  


def revisar_letra (palabra_sec, palabra, letra):
  lista_palabra_sec = []
  lista_palabra = []
  indices_sec = []
  resultado = ""
  
  for a in palabra_sec:
    lista_palabra_sec.append(a)
  
  for n in range(len(palabra)):
    lista_palabra.append(palabra[n])
    if palabra[n] == "_":
      indices_sec.append(n)
  
  for i in indices_sec:
    if lista_palabra_sec[i] == letra:
      lista_palabra[i] = letra
  
  for a in lista_palabra:
    resultado += a
  
  return resultado
  





palabras_secretas = ["evadirse", "lepidoptero", "bañarse", "cuaderno"]
indice_sec = random.randint(0, len(palabras_secretas) - 1)
intentos = 0

palabra_sec = palabras_secretas[indice_sec]



while intentos < 7:
  print(palabra)
  letra = input("Que letra tendra?: ")
  palabra = revisar_letra(palabra_sec, palabra, letra)
  
  if palabra == palabra_sec:
    print("Ganaste, la palabra era ",palabra_sec)
    break

  intentos += 1


if intentos == 7:
  print("Perdiste, la palabra era ", palabra_sec)