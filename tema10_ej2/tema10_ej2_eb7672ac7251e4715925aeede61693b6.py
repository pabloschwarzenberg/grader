#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    Lpalabra1=list(palabra1)
    Lpalabra2=list(palabra2)
    distancia=0
    i=0
    if len(palabra1)==len(palabra2):
        while i<len(palabra1):
            if Lpalabra1[i]==Lpalabra2[i]:
                pass
            else:
                distancia+=1
            i=i+1
    if len(palabra1)!=len(palabra2):
        for letra in Lpalabra1:
            if letra in Lpalabra2:
                if Lpalabra2.count(letra)>1:
                    distancia+=1
                pass
            else:
                distancia+=1
        for letra in Lpalabra2:
            if letra in Lpalabra1:
                if Lpalabra1.count(letra)>1:
                    distancia+=1
                pass
            else:
                distancia+=1
    if palabra1 == palabra2:
        return "0D"
    if distancia>1:
        return "+1"
    if distancia==1 and len(palabra1)!= len(palabra2):
        return "IB"
    if distancia==1 and len(palabra1)==len(palabra2):
        return "1S"

if __name__=="__main__":
    pass
           