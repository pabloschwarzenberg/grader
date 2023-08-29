#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass

if __name__=="__main__":
  import sys
  P1 = input("Palabra 1: ") #gato
  P2 = input("Palabra 2: ") #gatito

  if len(P1) == len(P2):
      distancia = 0
      for i in P1:
          distancia = P2.count(i) - P1.count(i)
          if distancia != 0:
              print("+1")
              sys.exit()
      print("0D")

  elif len(P1) > len(P2) or len(P1) < len(P2):
      if len(P1) - len(P2) == 1:
          print("1S")
      else:
          print("+1")
           