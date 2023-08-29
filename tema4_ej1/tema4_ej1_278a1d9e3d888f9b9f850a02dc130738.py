from random import randint

def ocultarletras(palabra, cantidad):
    palabra = "lepidoptero"
    acumula = []
    palabra = list(palabra)
    while cantidad != 0:
      x = randint(1,len(palabra)-1)
      if x not in acumula:
          acumula.append(x)
          cantidad = 1
          palabra[x] = ""
          palabra = "".join(palabra)
          return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    x = list(palabra_secreta)
    palabra = list(palabra)
    if letra in x:
        y = palabra_secreta.find("_")
        palabra[y] = letra
        palabra = "".join(palabra)
        print(palabra)
        return palabra