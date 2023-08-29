import math
def interpretar(expresion,ordenado=None):
    if ordenado==None:
        expresion=list(expresion)
        n=0
        while n<len(expresion):
            if expresion[n].isdigit():
                m=n
                while n+1<len(expresion) and expresion[n+1].isdigit():
                    expresion[m]=expresion[m]+expresion[n+1]
                    expresion.remove(expresion[n+1])    
            n+=1
    try:
        indice=expresion.index("*")
        try:
            indice=expresion.index("/")
            if expresion.index("*")<indice:
                indice=expresion.index("*")
            pass
        except ValueError:
            pass
    except ValueError:
        try:
            indice=expresion.index("/")
            pass
        except ValueError:
            try:
                indice=expresion.index("+")
                try:
                    indice=expresion.index("-")
                    if expresion.index("+")<indice:
                        indice=expresion.index("+")
                except ValueError:
                    pass
            except ValueError:
                try:
                    indice=expresion.index("-")
                except ValueError:
                    expresion="".join(expresion)
                    expresion=round(float(expresion),8)
                    return expresion
    if expresion[indice]=="*":
        expresion[indice]=str(float(expresion[indice-1])*float(expresion[indice+1]))
        expresion.pop(indice+1)
        expresion.pop(indice-1)
        return interpretar(expresion,"Nada")
    elif expresion[indice]=="/":
        expresion[indice]=str(float(expresion[indice-1])/float(expresion[indice+1]))
        expresion.pop(indice+1)
        expresion.pop(indice-1)
        return interpretar(expresion,"Nada")
    elif expresion[indice]=="+":
        expresion[indice]=str(float(expresion[indice-1])+float(expresion[indice+1]))
        expresion.pop(indice+1)
        expresion.pop(indice-1)
        return interpretar(expresion,"Nada")
    elif expresion[indice]=="-":
        expresion[indice]=str(float(expresion[indice-1])-float(expresion[indice+1]))
        expresion.pop(indice+1)
        expresion.pop(indice-1)
        return interpretar(expresion,"Nada")
            
    pass

resultado=interpretar("54+8/1+7/34")
print(resultado)
#el resultado debiera ser 15.66666
      