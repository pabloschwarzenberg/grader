from random import randint
      
def ocultar_letras(word, cantidad):

  word = "maquina"

  acumula = []

  word = list(word)

  while cantidad != 0:

    x = randint(1,len(word)-1)

    if x not in acumula:

     acumula.append(x)

     cantidad-=1

     word[x] = "_"

  word = "".join(word)

  return word



def revisar_letra(word_secreta,word,letra):

  x = list(word_secreta)

  word = list(word)

  if letra in x:

    y = word_secreta.find("-")

    word[y] = letra

  word = "".join(word)

  print(word)

  return word