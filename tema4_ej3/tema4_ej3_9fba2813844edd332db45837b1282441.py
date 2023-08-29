def jerigonzo(string):

  stringSalida = ""

  for letra in string:

   if letra.upper() == "A" or letra.upper() == "E" or letra.upper() =="I" or letra.upper() == "O" or letra.upper() == "U":

    stringSalida = stringSalida + letra + "p" + letra

   else:

    stringSalida = stringSalida + letra

     

  return stringSalida



if __name__ == "__main__":

  palabra = input("Ingrese la palabra a convertir a jerigonzo")

  j = jerigonzo(palabra)

  print("La palabra en jerigonzo es : ", j)

         