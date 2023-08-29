def es_vocal(texto):
    return texto in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
def jerigonzo(string):
    aux=""
    i=0
    for letra in string:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux

if __name__ == "__main__":
  j=input("palabra: ")
  r=jerigonzo(j)
  print(r)