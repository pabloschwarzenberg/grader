import random
palabra_secreta = ["tomas","gabriel","ashley","diego","lepidoptero"]
palabra = palabra_secreta[random.randint(0,len(palabra_secreta)-1)]
cantidad = random.randint(0,len(palabra))
palabrasecreta = palabra
palabra = list(palabra)

def ocultar_letras(palabra, cantidad):
  b = 0
  while b < cantidad:   
    x = random.randint(0,len(palabra)-1)
    if palabra[x] == "_":
      pass
    else:  
      palabra.pop(x)
      palabra.insert(x,"_")
      b += 1
  return palabra

def revisar_letra(palabrasecreta, letra):
  contador = 0
  while contador < 8:
    letra = input()
    if letra in palabra_secreta:
      break
    elif letra in palabra_original:
      p = palabra_original.find(letra)
      palabrasecreta.pop(p)
      palabrasecreta.insert(p, letra)
      print(palabrasecreta)
      if "_" not in palabrasecreta:
        palabra_original
        break
      else:
        continue
      contador += 1
    elif contador == 8:
      break
    else:
      contador +=1
  return palabra_original

if __name__ == "__main__":
    pass
         