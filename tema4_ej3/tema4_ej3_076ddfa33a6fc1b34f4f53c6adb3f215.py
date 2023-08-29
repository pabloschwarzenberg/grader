def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
        
def jerigonzo(string):
 convertido = []
 for palabra in string:
  for letra in palabra:
   if letra in "aeiouAEIOU":
    letra = letra + "p"+ letra
   convertido.append(letra)
 convertido = "".join(convertido)
 return convertido 