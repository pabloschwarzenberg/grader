def jerigonzo(string):
     convertir = []
     for  palabra in string:
          for letra in palabra:
               if letra in "aeiouAEIOU":
                    letra = letra + "p" + letra
               convertir.append(letra)
     convertir = "".join(convertir)           
     return convertir