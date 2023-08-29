#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  for a,b in (palabra1,palabra2):     
       for i,s in enumerate(difflib.ndiff(a, b)):
          if s[0]==' ': continue
          elif s[0]=='-':
              palabra1.split("_")
          elif s[0]=='+':
              palabra2.split("_")
      return (palabra1,palabra2)    


if __name__=="__main__":
    pass
           