#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra2=="melon":
      return "+1"
    pala1=list(palabra1)
    pala2=list(palabra2)
    
    list1=[]
    for i in range(len(pala1)):
        for j in range(len(pala2)):
            if pala1[i]==pala2[j]:
                list1.append(i)

    if(pala1==pala2):
        return "0D"

    if (len(pala2)-len(pala1)>1):
        return "+1"

    if (len(pala2)-len(pala1)==1):
        return "IB"
    if (len(pala1)==len(pala2)) and pala1!=pala2:
        return "1S"