#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    dist=0
    sacar=0
    cambiar=0
    indice=0
    for caracter in palabra1:
      if indice>=len(palabra2) or indice+1>=len(palabra2):
        break
      sacar=abs(len(palabra1)-len(palabra2))
      if caracter!=palabra2[indice] and len(palabra1)==len(palabra2):
        dist+=1
        cambiar+=1
      if (caracter!= palabra2[indice] and caracter!=palabra2[indice+1])  and len(palabra1)!=len(palabra2):
          dist+=1
      indice+=1
    dist+=sacar
    if dist>1 or cambiar>1 or sacar>1:
        return "+1"
    elif dist==1 and sacar==1:
        return "IB"
    elif dist==1 and cambiar==1:
        return "1S"
    elif dist==0:
        return "0D"

if __name__=="__main__":
    pass
           