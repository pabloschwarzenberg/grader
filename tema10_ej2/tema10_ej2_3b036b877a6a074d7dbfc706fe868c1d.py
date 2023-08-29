#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def distancia(palabra1,palabra2):
    i=0
    a=0
    if len(palabra1)<len(palabra2):
     while (len(palabra1))>i:
            if palabra1[i]!=palabra2[i]:
                a=a+1
                print("sss")
            i=i+1
     a=a+(len(palabra2)-len(palabra1))
    else:
        while (len(palabra2))>i:
            if palabra1[i]!=palabra2[i]:
                a=a+1
                print("sss")
            i=i+1
        a=a+(len(palabra2)-len(palabra1))
    return a
def agrega(p1,p2):
    print(len(p1),len(p2))
    if len(p1)>len(p2):
        i=0
        for jaja in p2:
            if (jaja in p1)==False:
                i=i+1
    elif len(p2)>len(p1):
        i=0
        for jaja in p1:
            if (jaja in p2)==False:
                i=i+1
    i=i+abs(len(p1)-len(p2))
    return i
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return "0D"
    elif len(palabra1)==len(palabra2):
        if distancia(palabra1, palabra2)==1:
            return "1S"
        else:
            return "+1"
    elif distancia(palabra1,palabra2)==1:
        return "IB"
    else:
        if agrega(palabra1,palabra2)==1:
            return "IB"
        else:
         return "+1"
    pass

if __name__=="__main__":
   print(levenshtein("lala","lala"))
   print(levenshtein("lala","lalo"))
   print(distancia("lala","lalo"))
   print(levenshtein("jaron","jarron"))
   pass
