#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    len1=len(palabra1)
    len2=len(palabra2)
    m=0
    STR=""
    STR1=""
    STR2=""
    if len1==len2:
        while m<len1:
            if palabra1[m]==palabra2[m]:
                m=m+1
            elif palabra1[m]!=palabra2[m]:
                STR=STR+palabra1[m]
                m=m+1
        if len(STR)>1:
            return("+1")
        if len(STR)==1:
            return("1S")
        if len(STR)==0:
            return("0D")

    if len1>len2:
        if len1==len2+1:
            while m<len2:
                if palabra1[m]==palabra2[m]:
                    m=m+1
                    STR1=STR1
                    STR2=STR2
                elif palabra1[m]!=palabra2[m]:
                    elemento_borrado=palabra1[m]
                    STR=STR+elemento_borrado
                    STR1=STR1+"1"
                    STR2=STR2
                    m=m+1
                    while m<len2:
                        if palabra2[m-1]==palabra1[m]:
                            m=m+1
                        else:
                            return("+1")
            if STR1==STR2:
                return("IB")
            
            if len(STR)==1:
                return("IB")
            if len(STR)>1:
                return("+1")
        else:
            return("+1")

    if len1<len2:
        if len1+1==len2:
            while m<len1:
                if palabra1[m]==palabra2[m]:
                    m=m+1
                    STR1=STR1
                    STR2=STR2
                elif palabra1[m]!=palabra2[m]:
                    elemento_borrado=palabra2[m]
                    STR=STR+elemento_borrado
                    STR1=STR1
                    STR2=STR2+"1"
                    m=m+1
                    while m<len1:
                        if palabra1[m-1]==palabra2[m]:
                            m=m+1
                        else:
                            return("+1")

            if STR1==STR2:
                return("IB")
   
            if len(STR)==1:
                return("IB")
            if len(STR)>1:
                return("+1")
        else:
            return("+1")
    
