#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    l1=len(palabra1)
    l2=len(palabra2)
    lp1=list(palabra1)
    lp2=list(palabra2)
    print(lp1,lp2)
    if l1==l2:
        B=1
    else:
        B=0
        DB=abs(l1-l2)
    restart=True
    for r in range(0,l1):
        for i in range(0,l2):            
            if lp1[r]==lp2[i]:
                lp1[r]='1'
                lp2[i]='0'
                print(lp1,lp2)
    l1=(l1)-lp1.count('1')
    l2=(l2)-lp2.count('0')
    
    if B==1:
        if l1>1:
            return'+1'
        elif l1==1:
            return'1S'
        elif l1==0:
            return'0D'
    elif B==0:
        if DB>1:
            return'+1'
        elif DB==1:
            if l1>l2:
                if l1>1:
                    return'+1'
                elif l1==1:
                    return'IB'
            elif l2>l1:
                if l2>1:
                    return'+1'
                elif l2==1:
                    return'IB'
    pass

if __name__=="__main__":
    pass