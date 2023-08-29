import random

palabra_secreta = ["tomas","gabriel","ashley","diego","lepidoptero"]
palabra = palabra_secreta[random.randint(0,len(palabra_secreta)-1)]
cantidad = int(input("cantidad de letras que quiera ocultar: "))
palabra_original = palabra
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

def revisar_letra(palabra, letra):
  contador = 0
  while contador < 8:
    letra = input()
    if letra in palabra_secreta:
      break
    elif letra in palabra_original:
      p = palabra_original.find(letra)
      palabra.pop(p)
      palabra.insert(p, letra)
      print(palabra)
      if "_" not in palabra:
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

print(ocultar_letras(palabra,cantidad))
letra = print("Ingrese una letra")

revisar_letra(palabra,letra)