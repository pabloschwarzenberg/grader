#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):

    i=0
    cuenta=0
    L1=len(palabra1)
    L2=len(palabra2)

    if L1==L2:
        while i<L1:
            if palabra1[i]!=palabra2[i]:
                cuenta=cuenta+1
                i=i+1
                if i==L1:
                    break
                continue
            
            else:
                i=i+1
                if i==L1:
                    break
                continue
        if cuenta==0:
            return("0D")
        elif cuenta==1:
            return("1S")
        elif cuenta>1:
            return("+1")

    elif (L1-L2)**2==1:

        g=0

        
        palabra1=sorted(palabra1)
        palabra2=sorted(palabra2)

        
        if L1<L2:
            palabra1.append("_")
            palabra1="".join(palabra1)
            palabra2="".join(palabra2)
    
        elif L1>L2:
            palabra2.append("_")
            palabra1="".join(palabra1)
            palabra2="".join(palabra2)
            
        p_1=palabra1.count("_")
        p_2=palabra2.count("_")
            
        while g<=L1:

            if palabra1[g]!=palabra2[g]:
                if p_1==1:
                    palabra1=list(palabra1)
                    palabra2=list(palabra2)
                    palabra1.pop()
                    palabra2.pop(g)
                    palabra1="".join(palabra1)
                    palabra2="".join(palabra2)

                    if palabra1==palabra2:
                        return("IB")
                    else:
                        return("+1")

                elif p_2==1:
                    palabra1=list(palabra1)
                    palabra2=list(palabra2)
                    palabra2.pop()
                    palabra1.pop(g)
                    palabra1="".join(palabra1)
                    palabra2="".join(palabra2)

                    if palabra1==palabra2:
                        return("IB")
                    else:
                        return("+1")

            else:
                g=g+1
                continue

                
                    
                
                

    else:
        return ("+1")
           