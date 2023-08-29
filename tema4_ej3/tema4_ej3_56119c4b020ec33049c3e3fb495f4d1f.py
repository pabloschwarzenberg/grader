def jerigonzo(string):
  a = "a"
  e = "e"
  i = "i"
  o = "o"
  u = "u"
  lista = []

  for x in string:
    lista.append(x)

  for y in range(len(lista)):
    ind = lista[y]
    print(ind)
    if ind == a or ind == e or ind == i or ind == o or ind == u:
      lista[y] = ind+"p"+ind
  string = "".join(lista)
  return string
         