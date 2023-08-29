def jerigonzo(string):

  lista_texto = list(string) 
  vocales=['a','e','i','o','u']

  jeri = str()

  for i in lista_texto:
    for vocal in vocales:
      if vocal == i:
        jeri = jeri + i + "p" 
    jeri = jeri + i

  return jeri

if __name__ == "__main__":

  string = input('Escriba aqui: ')
  resultado = jerigonzo(string)
  print(resultado)