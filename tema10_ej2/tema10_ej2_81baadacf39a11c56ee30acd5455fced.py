#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    palabra1=list(palabra1)
    palabra2=list(palabra2)
    contador=[]
    chica=[]
    grande=[]
    if len(palabra1)<=len(palabra2):
        for i in range(len(palabra1)):
            chica.append(palabra1[i])
        for i in range(len(palabra2)):
            grande.append(palabra2[i])
    if len(palabra2)<len(palabra1):
        for i in range(len(palabra1)):
            grande.append(palabra1[i])
        for i in range(len(palabra2)):
            chica.append(palabra2[i])
            
    #if len(palabra1)!=len(palabra2):
    #    for i in range(len(chica)):
    #        if chica[i] in grande:
    #            contador.append(palabra1[i])
    #for i in range(min(len(palabra1),len(palabra2))):
    #    if palabra1[i]==palabra2[i]:
    #        continue
    #    elif palabra1[i]!=palabra2[i]:
    #        contador.append(palabra1[i])
    #        continue
    k=0
    for i in range(len(grande)):
        k=0
        for a in range(len(chica)):
            if chica[a]==grande[i]:
                chica[a]=" "
                k=1
                break
            else:
                k=0
        if k==0:
            contador.append(grande[i])
    
    if len(palabra1)==len(palabra2):
        if palabra1==palabra2 and len(contador)==0:
            return "0D"
        elif palabra1!=palabra2 and len(contador)==1:
            return "1S"
        elif palabra1!=palabra2 and len(contador)>1:
            return "+1"
    elif len(palabra1)!=len(palabra2):
        print(contador)
        p1=len(palabra1)-len(palabra2)
        if (p1==1 or p1==-1) and len(contador)==1:
            return "IB"
        elif (p1==1 and len(contador)>1) or (p1==-1 and len(contador)>1):
            return "+1"
        elif p1>1 or p1<-1:
            return "+1"
if __name__=="__main__":
    #palabra=levenshtein("gallina","gallina")
    #print(palabra)
    #palabra4=levenshtein("jarro","jarr")
    #print(palabra4)
    #palabra5=levenshtein("gato","gatito")
    palabra6=levenshtein("jarron","melon")
    #print(palabra5)
    print(palabra6)
    #palabra8=levenshtein("caro","cara")
    #palabra9=levenshtein("Limon","limon")
    #print(palabra8)
    #print(palabra9)