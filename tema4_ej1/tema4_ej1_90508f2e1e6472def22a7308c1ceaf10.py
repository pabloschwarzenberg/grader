from random import randint
def ocultar_letras(palabra,cantidad):
  palabra = "robot"
  lista = []
  palabra = list(palabra)
  while cantidad != 0:
   H = randint(1, len(palabra)-1)
   if H not in lista:
      lista.append(H)
      cantidad-=1
         palabra[H] = "_"
   palabra = " ".join(palabra)
  return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
  H = list(palabra_secreta)
  palabra = list(palabra)
  if letra in H:
    x = palabra_secreta.find("-")
    palabra[x] = letra
  palabra = " ".join(palabra)
  print(palabra)
  return palabra

if __name__ == "__main__":
    pass
         