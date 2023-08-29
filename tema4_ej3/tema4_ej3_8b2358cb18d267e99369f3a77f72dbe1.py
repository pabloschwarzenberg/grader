def jerigonzo(string):
  Vocales="AEIOUaeiou"
  texto=[]
  for i in string:
    if i in Vocales:
      i=i+"p"+i
    texto.append(i)
  return "".join(texto)

if __name__ == "__main__":
    pass