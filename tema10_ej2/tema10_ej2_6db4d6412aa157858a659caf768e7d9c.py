#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def encuentra(cadena, carac, inicio=0, paso=1):
    indice = inicio
    while 0 <= indice < len(cadena):
        if cadena[indice] == carac:
            return indice
        indice += paso
    return carac
    
def levenshtein(cadena,palabra):
  l=[]
  cont=0
  for j in palabra:
    fol=(encuentra(cadena,j))
    l.append(fol)
  for i in range(len(l)):
    if isinstance(l[i], str)==True:
      cont+=1
  x=set(l)
  dup=[]
  for c in x:
    if l.count(c)>1:
        dup.append(c)
  if len(dup)==0  and not cont==1:
    sol="+"+str(1)
  else:
    if cont==1:
      if len(dup)==0:
        sol=str(cont)+"S"
      else:
        sol="+"+str(cont)
    elif cont==0:
      if len(dup)==1:
        if dup[0]==2:
          sol="IB"
        else:
          sol=str(1)+"S"
      else:
        sol=str(cont)+"D"
  return (sol)
if __name__=="__main__":
    levenshtein(input(),input())
           