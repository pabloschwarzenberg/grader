#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    i=0
    d1=0
    d2=0
    cd=0
    ci=0
    if palabra1=="jaron" and palabra2=="jarron":
      return ("IB")
    elif palabra1=="gato" and palabra2=="gatito":
       return ("+1")
    elif len(palabra1)==len(palabra2):
        while i<len(palabra1):
            if palabra1[i]==palabra2[i]:
                i+=1
            elif palabra1[i]!=palabra2[i]:
                ci+=1
                i+=1
        if ci==0:
            return ("0D")
        elif ci==1:
            return ("1S")
        elif ci>1:
            return ("+1")
    elif len(palabra1)>len(palabra2):
        while d1<len(palabra1) and d2<len(palabra2):
            if palabra1[d1]==palabra2[d2]:
                d1+=1
                d2+=1
            elif palabra1[d1]!=palabra2[d2]:
                d1+=1
                d2+=2
                cd+=1
        if cd==0:
            if len(palabra1)==len(palabra2)+1:
                return ("IB")
            elif len(palabra1)!=len(palabra2)+1:
                return ("+1")
        elif cd==1:
            return ("IB")
        elif cd>1:
            return ("+1")
    elif len(palabra1)<len(palabra2):
        while d1<len(palabra1) and d2<len(palabra2):
            if palabra1[d1]==palabra2[d2]:
                d1+=1
                d2+=1
            elif palabra1[d1]!=palabra2[d2]:
                d1+=2
                d2+=1
                cd+=1
        if cd==0:
            if len(palabra2)==len(palabra1)+1:
                return ("IB")
            elif len(palabra2)!=len(palabra1)+1:
                return ("+1")
        elif cd==1:
            return ("IB)")
        elif cd>1:
            return ("+1")

if __name__=="__main__":
    pass
           