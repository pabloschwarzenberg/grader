def jerigonzo(string):
  vocales = ['a','e','i','o','u']
  lista_letras = list(string)
  for indice,letras in enumerate(lista_letras):
      if letras in vocales and letras != vocales :
          lista_letras[indice] = vocales[vocales.index(letras)]
      if letras in vocales and letras == vocales :
         lista_letras[indice] = vocales[0]
  string_nueva = "p".join(lista_letras)
  return string_nueva
 


if __name__ == "__main__":
    pass
         