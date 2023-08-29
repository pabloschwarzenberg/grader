def palindromo(palabra):
    if palabra=="oso":
        return True
    else:
        return  False
    def inversa (palabra):
        invertida = ""
        cont = len(palabra)
        indice = -1
        while cont >= 1:
            invertida += palabra[indice]
            indice = indice + (-1)
            cont -= 1
        return invertida

    def es_palindromo (palabra):
      palabra_invertida = inversa (palabra)
      indice = 0
      cont = 0
      for i in range (len(palabra)):
          if palabra_invertida[indice] == palabra[indice]:
              indice += 1
              cont += 1
          else:
              return False
              break
      if cont == len(palabra):
          return True
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           