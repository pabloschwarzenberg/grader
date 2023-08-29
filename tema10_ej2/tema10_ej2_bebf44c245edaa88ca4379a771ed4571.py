#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    largo1=len(palabra1)
    largo2=len(palabra2)
    lista1=list(palabra1)
    lista2=list(palabra2)
    i=0
    
    if largo1==largo2:
      if palabra1==palabra2:
        return "0D"
      else:
        for n in lista1:
          if not n in lista2:
            i+=1
        if i==1:
          return "1S"
        else:
          return "+1"
              
    if largo1!=largo2:
        if largo1>largo2:
          i=largo1-largo2
        else:
          i=largo2-largo1
        for n in lista1:
          if not n in lista2:
            i+=1
        if i==1:
          return "IB"
        else:
          return "+1"

if __name__=="__main__":
    palabra1=input()
    palabra2=input()
    resultado=levenshtein(palabra1,palabra2)
    print(resultado)
           