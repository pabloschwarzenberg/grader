import random
def ocultar_letras(palabra,cantidad):
  f = random.randint(0,len(palabra))
  l = []
  for b in palabra:
    l.append(palabra)
  for a in range(cantidad):
    l[random.randint(0,len(palabra))] = "_"
  return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
  indice = 0
  for i in palabra_secreta:
    if palabra in letra:
      indice = palabra.find(letra,indice + 1)
      palabra[indice] = letra

  return palabra

if __name__ == "__main__":
  palabra = input()
  cantidad = int(input())
  print(ocultar_letras(palabra,cantidad))
  palabra_secreta = input()
  letra = input()
  print(revisar_letra(palabra_secreta,palabra,letra))
         