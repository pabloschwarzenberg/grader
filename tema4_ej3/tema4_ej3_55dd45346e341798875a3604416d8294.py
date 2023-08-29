def jerigonzo(string):
  vocales = ["a", "e", "i", "o", "u"]
  string_jg = ""
  aux = []
  for i in string:
    aux.append(i)
  for caracter in range(len(aux)):
    if aux[caracter] in vocales:
      aux[caracter] = aux[caracter] + "p" + aux[caracter]
  for i in aux:
    string_jg += i
  return string_jg

if __name__ == "__main__":
    frase = input("Ingrese una frase:")
    print(jerigonzo(frase))