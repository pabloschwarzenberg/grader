#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def funcion(p1,p2):
    if len(p1)<len(p2):
      return funcion(p2,p1)
    
    if len(p2)==0:
      return len(p1)
    
    previous_row = range(len(p2)+1)
    for i,c1 in enumerate(p1):
      current_row = [i + 1]
      for j,c2 in enumerate(p2):
          insertions = previous_row[j+1]+1
          deletions = current_row[j]+1
          substitutions = previous_row[j]+(c1!=c2)
          current_row.append(min(insertions,deletions,substitutions))
      previous_row = current_row
    
    return previous_row[-1]
  
def levenshtein(p1,p2):
    if funcion(p1,p2) == 0:
      return "0D"
    elif funcion(p1,p2) == 1:
      if len(p1) == len(p2):
        return "1S"
      else:
        return "IB"
    elif funcion(p1,p2) > 1:
      return "+1"

if __name__=="__main__":
  p1 = input()
  p2 = input()
  
  pass