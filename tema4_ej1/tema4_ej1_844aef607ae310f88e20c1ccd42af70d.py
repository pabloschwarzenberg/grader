import random
def ocultar_letras(palabra,cantidad):
  n=0
  while n<cantidad: 
    letra = random.randint(0,cantidad)
    le = palabra[letra]
    palabra = palabra.replace(le,"_",1)
    n +=1
  return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    n = 0
    while n<len(letra):
      if letra in palabra:
        x = palabra.find(letra)
        print(x)
        pal = palabra_secreta[x]
        palabra = palabra_secreta.replace(pal,letra,1)
      else:
        palabra = palabra_secreta
      n += 1
    return palabra


if __name__ == "__main__":
    pass
         