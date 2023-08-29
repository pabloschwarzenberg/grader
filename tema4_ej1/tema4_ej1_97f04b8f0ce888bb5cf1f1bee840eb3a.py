import random
def ocultar_letras(palabra,cantidad):
    Lista = []
    while len(Lista) < cantidad:
      Numero = random.randint(0,(len(palabra)-1))
      if Numero not in Lista:
        Lista.append(Numero)
    Lista_palabra = []
    for Letra in palabra:
      Lista_palabra.append(Letra)
   
    for Numero in Lista:
      Lista_palabra[Numero] = "_"
    return "".join(Lista_palabra)
def revisar_letra(palabra_secreta,palabra,letra):
    Lista_palabra = []
    
    for Letra in palabra:
      Lista_palabra.append(Letra)
    for Posicion in range(len(palabra)):
       if letra == palabra_secreta[Posicion]:
         Lista_palabra[Posicion] = letra
    return "".join(Lista_palabra)         