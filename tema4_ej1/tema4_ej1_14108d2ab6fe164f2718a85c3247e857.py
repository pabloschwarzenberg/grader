import random

def ocultar_letras(palabra, cantidad):
  palabra = list(palabra)
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
    
def revisar_letra(palabra_secreta,palabra, letra):
    palabra_secreta = list(palabra)
    contador = 0
    letra = str()
    while contador < 8:
        if letra in palabra_secreta:
            return palabra
            break       
        elif letra in palabra_secreta:
            p = palabra_secreta.find(letra)
            palabra.pop(p)
            palabra.insert(p, letra)
            return palabra
            if "_" not in palabra:
                return palabra
                break
            else:
                return palabra
                continue
            contador += 1
        elif contador == 8:
            return palabra
            break
        else:
            contador +=1
            return palabra