#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son igualesdef levenshtein(palabra1,palabra2):
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return '0D'
    elif len(palabra1)==len(palabra2):
        n=0
        m=0
        for letra in palabra1:
            if letra==palabra2[n]:
                n=n+1
            elif letra!=palabra2[n]:
                n=n+1
                m=m+1
        if m==1:
            return '1S'
        else:
            return '+1'
    elif len(palabra1)-len(palabra2)>=2 or len(palabra2)-len(palabra1)>=2:
        return '+1'
    elif (len(palabra1)-len(palabra2))==1:
        l=0
        p=0
        for letra in palabra1:
            palabra2=palabra2+' '
            if letra==palabra2[l]:
                l=l+1
            elif letra!=palabra2[l]:
                p=p+1
        if p==1:
            return 'IB'
        else:
            return '+1'
    elif (len(palabra2)-len(palabra1))==1:
        q=0
        r=0
        for letra in palabra2:
            palabra1=palabra1+' '
            if letra==palabra1[q]:
                q=q+1
            elif letra!=palabra1[q]:
                r=r+1
        if r==1:
            return 'IB'
        else:
            return '+1'
           