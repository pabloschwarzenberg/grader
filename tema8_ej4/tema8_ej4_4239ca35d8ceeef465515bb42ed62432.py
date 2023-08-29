def rot13(palabra):
  suma=""
  for n in palabra:
    if n in lista1:
      print(n,"estoy en lista 1")
      indice = lista1.index(n)
      print(indice)
      suma+=lista2[indice]
    if n in lista2:
      print(n,"estoy en lista 2")
      indice = lista2.index(n)
      print(indice)
      suma+=lista1[indice]
  return suma
lista1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
lista2=['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
if __name__ == "__main__":
  palabra=input("ingrese palabra: ")
  print(rot13(palabra))
           