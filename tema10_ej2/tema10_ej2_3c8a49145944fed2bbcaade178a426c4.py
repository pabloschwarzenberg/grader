#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1)==len(palabra2):
        l=[]
        s=[]
        for i in palabra1:
            l.append(i)
        for j in palabra2:
            s.append(j)
        c=0
        for i in range(len(palabra1)):
            if palabra1[i]!= palabra2[i]:
                c+=1
        if c==1:
            return "1S"

    if len(palabra1)==len(palabra2)+1 or len(palabra1)+1==len(palabra2):
        l=[]
        s=[]
        for i in palabra1:
            l.append(i)
        for j in palabra2:
            s.append(j)
        for letra in l:
            try:
                s.remove(letra)
            except:
                break
        if len(s)==1:
            return "IB"
        for letra in s:
            try:
                l.remove(letra)
            except:
                break
        if len(l)==1:
            return "IB"

    if palabra1==palabra2:
        return "0D"
    else:
        return "+1"

if __name__=="__main__":
    palabra1= "gato"
    palabra2= "gatito"
    print(levenshtein(palabra1, palabra2))
    palabra1= "hola"
    palabra2= "ola"
    print(levenshtein(palabra1, palabra2))
    palabra1= "gallina"
    palabra2= "gallina"
    print(levenshtein(palabra1, palabra2))
    palabra1= "caro"
    palabra2= "cara"
    print(levenshtein(palabra1, palabra2))
    palabra1= "Limon"
    palabra2= "limon"
    print(levenshtein(palabra1, palabra2))
           