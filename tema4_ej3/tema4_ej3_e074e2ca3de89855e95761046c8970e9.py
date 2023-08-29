def jerigonzo(texto):
  vocales = ['a','e','i','o','u']
  auxiliar = ''
  for var in texto:
    if var in vocales:
      auxiliar += var+'p'+var
    elif var not in vocales:
      auxiliar += var
  return auxiliar
if __name__ == "__main__":
    texto = input('Ingrese un texto: ')
    jerigonzo()