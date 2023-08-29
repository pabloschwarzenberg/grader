def jerigonzo(string):
  palabra = string
  lista = list(palabra)
  largoLista = len(lista)
  i = 0
  while (i < largoLista):
      if(lista[i] == "a" or lista[i] == "e" or lista[i] == "i" or lista[i] == "o" or lista[i] == "u"):
        aux = lista[i]
        lista[i] += "p"
        lista[i] += aux
      i += 1
  palabra = ""
  i = 0
  while (i < largoLista):
       palabra += lista[i]
       i += 1
  return palabra
    

if __name__ == "__main__":
    pass
         